#!/usr/bin/env bash

# =========================================================
# Parla Italiano Scenario Organizer
# =========================================================
#
# Safely reorganizes exported scenario JSON files into:
#
# category/scenario/
#
# Example:
#
# travel_airport_arrival_vocabulary.json
#
# becomes:
#
# travel/
# └── airport_arrival/
#     └── travel_airport_arrival_vocabulary.json
#
# Features:
# - Dry-run mode
# - Collision protection
# - Filename validation
# - Logging
# - Strict error handling
# - Safe with Git
# - Never overwrites existing files
#
# =========================================================

set -Eeuo pipefail

# -----------------------------
# CONFIG
# -----------------------------

DRY_RUN=false
VERBOSE=true
LOG_FILE="organize_scenarios.log"

# -----------------------------
# COLORS
# -----------------------------

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# -----------------------------
# LOGGING
# -----------------------------

log() {
  echo -e "$1" | tee -a "$LOG_FILE"
}

info() {
  log "${BLUE}[INFO]${NC} $1"
}

success() {
  log "${GREEN}[SUCCESS]${NC} $1"
}

warn() {
  log "${YELLOW}[WARNING]${NC} $1"
}

error() {
  log "${RED}[ERROR]${NC} $1"
}

# -----------------------------
# ERROR HANDLER
# -----------------------------

trap 'error "Script failed at line $LINENO."' ERR

# -----------------------------
# HELP
# -----------------------------

usage() {
  cat <<EOF

Usage:
  ./organize_scenarios.sh [OPTIONS]

Options:
  --dry-run     Preview changes without moving files
  --quiet       Reduce console output
  --help        Show this help message

Examples:
  ./organize_scenarios.sh --dry-run
  ./organize_scenarios.sh

EOF
}

# -----------------------------
# ARGUMENT PARSING
# -----------------------------

while [[ $# -gt 0 ]]; do
  case "$1" in
  --dry-run)
    DRY_RUN=true
    shift
    ;;
  --quiet)
    VERBOSE=false
    shift
    ;;
  --help)
    usage
    exit 0
    ;;
  *)
    error "Unknown argument: $1"
    usage
    exit 1
    ;;
  esac
done

# -----------------------------
# PRECHECKS
# -----------------------------

if [[ ! -d "." ]]; then
  error "Invalid working directory."
  exit 1
fi

json_count=$(find . -maxdepth 1 -type f -name "*.json" | wc -l)

if [[ "$json_count" -eq 0 ]]; then
  warn "No JSON files found."
  exit 0
fi

info "Found $json_count JSON files."

# -----------------------------
# MAIN PROCESS
# -----------------------------

moved_count=0
skipped_count=0

for file in *.json; do

  [[ -f "$file" ]] || continue

  filename="${file%.json}"

  # Expected format:
  # category_scenario_type.json
  #
  # Example:
  # travel_airport_arrival_vocabulary.json

  if [[ ! "$filename" =~ ^[a-z0-9]+_.+_(vocabulary|phrases|sentences)$ ]]; then
    warn "Skipping malformed filename: $file"
    skipped_count=$((skipped_count + 1))
    continue
  fi

  # Extract category
  category="${filename%%_*}"

  # Remove category prefix
  remainder="${filename#*_}"

  # Remove suffix
  scenario="$(echo "$remainder" | sed -E 's/_(vocabulary|phrases|sentences)$//')"

  target_dir="$category/$scenario"
  target_file="$target_dir/$file"

  if [[ "$VERBOSE" == true ]]; then
    info "Processing: $file"
  fi

  # Create directory safely

  if [[ ! -d "$target_dir" ]]; then

    if [[ "$DRY_RUN" == true ]]; then
      info "[DRY RUN] Would create directory: $target_dir"
    else
      mkdir -p "$target_dir"
      info "Created directory: $target_dir"
    fi

  fi

  # Collision protection

  if [[ -e "$target_file" ]]; then
    warn "Target already exists, skipping: $target_file"
    skipped_count=$((skipped_count + 1))
    continue
  fi

  # Move file

  if [[ "$DRY_RUN" == true ]]; then

    info "[DRY RUN] Would move:"
    echo "  $file"
    echo "  -> $target_file"

  else

    mv -- "$file" "$target_file"
    success "Moved: $file -> $target_file"

  fi

  moved_count=$((moved_count + 1))

done

# -----------------------------
# SUMMARY
# -----------------------------

echo
success "Organization completed."

echo "----------------------------------------"
echo "Moved files   : $moved_count"
echo "Skipped files : $skipped_count"
echo "Dry run       : $DRY_RUN"
echo "Log file      : $LOG_FILE"
echo "----------------------------------------"
