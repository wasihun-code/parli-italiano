import json
import os

BENCHMARKS = [
    "accommodation/apartment_key_pickup",
    "accommodation/hotel_check_in",
    "travel/airport_arrival",
    "social/phone_call",
    "tech/buying_a_sim_card",
    "workstudy/job_interview",
    "shopping/clothing_store",
    "daily_life/at_the_bank",
    "health/doctor_appointment",
    "culture/museum_tickets"
]

def get_stats(slug):
    base_dir = f"src/data/exports/{slug}"
    
    # Conversations
    with open(f"{base_dir}/conversations.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        convs = data["conversations"] if isinstance(data, dict) and "conversations" in data else data
        conv_count = len(convs)
        total_turns = sum(len(c.get("messages", [])) for c in convs)

    # Lessons
    with open(f"{base_dir}/mini_lessons.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        lessons = data["lessons"] if isinstance(data, dict) and "lessons" in data else data
        lesson_count = len(lessons)

    # Linguistic
    prefix = slug.replace("/", "_")
    with open(f"{base_dir}/{prefix}_vocabulary.json", "r", encoding="utf-8") as f:
        vocab = json.load(f)
        vocab_count = len(vocab)
        untranslated_vocab = sum(1 for v in vocab if not v.get("english"))

    return {
        "conv_count": conv_count,
        "total_turns": total_turns,
        "lesson_count": lesson_count,
        "vocab_count": vocab_count,
        "untranslated_vocab": untranslated_vocab
    }

def main():
    benchmarks_data = {}
    for b in BENCHMARKS:
        print(f"Generating benchmark baseline for {b}...")
        benchmarks_data[b] = get_stats(b)

    with open("benchmarks/baseline.json", "w", encoding="utf-8") as f:
        json.dump(benchmarks_data, f, indent=2)
    
    print("Baseline generated in benchmarks/baseline.json")

if __name__ == "__main__":
    main()
