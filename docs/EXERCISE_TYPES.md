# Exercise Types Registry

Learning System V3 formally defines and structures the available exercise types into cognitive categories.

## Recognition Phase
1. **Listen**
   - *Objective:* Map spoken audio to Italian text and English meaning.
   - *Input:* Audio, Italian Text (hidden), English Text.
   - *Output:* Audio playback confirmation.
   - *Mastery Contribution:* +0.1 (FSRS Ease)

2. **Listen & Choose**
   - *Objective:* Identify correct English meaning from spoken Italian.
   - *Input:* Audio, 4 English Text options.
   - *Output:* Multiple choice selection.
   - *Mastery Contribution:* +0.2

3. **Match** (Multiple Choice)
   - *Objective:* Identify correct Italian from English prompt.
   - *Input:* English text prompt, 4 Italian text options.
   - *Output:* Multiple choice selection.
   - *Mastery Contribution:* +0.2

## Recall Phase
4. **Build Sentence** (Assembly)
   - *Objective:* Reconstruct syntax from known words.
   - *Input:* English prompt, scrambled Italian words.
   - *Output:* Ordered Italian array.
   - *Mastery Contribution:* +0.4

5. **Recall** (Fill-in-the-blank)
   - *Objective:* Retrieve specific vocabulary within context.
   - *Input:* Italian sentence with missing word, English translation.
   - *Output:* Selected missing word or typed word.
   - *Mastery Contribution:* +0.4

## Production Phase
6. **Dictation**
   - *Objective:* Exact transcription of spoken Italian.
   - *Input:* Audio.
   - *Output:* Typed Italian text.
   - *Mastery Contribution:* +0.8

7. **Speaking**
   - *Objective:* Pronunciation and verbal recall.
   - *Input:* Italian text (or English prompt).
   - *Output:* Web Speech API transcript matching target.
   - *Mastery Contribution:* +1.0

8. **Spelling**
   - *Objective:* Exact spelling without audio crutch.
   - *Input:* English prompt.
   - *Output:* Typed Italian text.
   - *Mastery Contribution:* +0.8

## Application Phase
9. **Reading**
   - *Objective:* Contextual comprehension without translation.
   - *Input:* Italian text.
   - *Output:* Continuation trigger.
   - *Mastery Contribution:* +0.1

10. **Conversation**
    - *Objective:* Situational branching dialogue.
    - *Input:* Host audio/text, 3 User choices.
    - *Output:* Selected situational reply.
    - *Mastery Contribution:* +1.0 (Implicit Mastery to underlying vocab)

11. **Review**
    - *Objective:* Spaced repetition maintenance.
    - *Input:* Variable based on FSRS state.
    - *Output:* Variable.
    - *Mastery Contribution:* FSRS decay reset.
