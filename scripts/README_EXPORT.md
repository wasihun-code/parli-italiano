# Scenario Questions Export

This script exports questions for all scenarios defined in `src/data/scenarios.ts` into JSON files.

## Usage

Run the following command to generate the exports:

```bash
npx tsx scripts/export_scenario_questions.ts
```

## Output

The script generates three JSON files for each scenario in `src/data/exports/`:

- `{category}_{scenario}_vocabulary.json`
- `{category}_{scenario}_phrases.json`
- `{category}_{scenario}_sentences.json`

## Format

Each item in the generated JSON files follows this format:

```json
{
  "id": "s1-v1-uscita",
  "italian": "uscita",
  "english": "exit",
  "type": "vocabulary",
  "choices": ["uscita", "bagagli", "controllo", "dogana"],
  "correctAnswer": "uscita",
  "feedback": {
    "correct": "Ottimo!",
    "incorrect": "Quasi! La risposta corretta è \"uscita\"."
  }
}
```

The `choices` array is shuffled and contains the correct Italian word plus 3 distractors from the same scenario if available.
