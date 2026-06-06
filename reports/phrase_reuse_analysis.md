# Phrase Reuse Analysis

- **Total Phrases:** 4647
- **Unique Phrases:** 4486
- **Phrase Reuse Rate:** 161 redundant occurrences
- **Compression Ratio:** 3.46%

### Top Repeated Phrases
- **Arrivederci!** (Count: 9, Scenarios: 8)
- **Grazie mille, arrivederci.** (Count: 8, Scenarios: 8)
- **Grazie, arrivederci!** (Count: 7, Scenarios: 7)
- **Grazie, buona giornata anche a lei.** (Count: 5, Scenarios: 5)
- **Arrivederci e buona giornata!** (Count: 4, Scenarios: 3)
- **Grazie mille per l'aiuto, buona giornata!** (Count: 4, Scenarios: 4)
- **Grazie, buona giornata!** (Count: 4, Scenarios: 3)
- **Grazie mille e arrivederci.** (Count: 3, Scenarios: 3)
- **Grazie mille, buona giornata.** (Count: 3, Scenarios: 2)
- **Grazie mille per l'aiuto. Arrivederci!** (Count: 3, Scenarios: 3)
- **Grazie, arrivederci e buona giornata.** (Count: 3, Scenarios: 3)
- **Grazie mille, a dopo.** (Count: 3, Scenarios: 3)
- **Arrivederci e grazie ancora!** (Count: 3, Scenarios: 3)
- **Arrivederci e buona serata!** (Count: 3, Scenarios: 3)
- **Ecco la mia carta d'identità. Va bene?** (Count: 2, Scenarios: 2)
- **Perfetto. Grazie mille per l'aiuto.** (Count: 2, Scenarios: 2)
- **Grazie mille per l'aiuto oggi.** (Count: 2, Scenarios: 2)
- **Grazie mille, buona giornata anche a lei. Arrivederci.** (Count: 2, Scenarios: 2)
- **Grazie ancora e buona giornata!** (Count: 2, Scenarios: 2)
- **Grazie anche a lei, arrivederci.** (Count: 2, Scenarios: 2)

### Architectural Answer
**Should phrases remain scenario-specific?**
For the vast majority (~90%), YES. Phrases are highly situational.

**Should common phrases become shared assets?**
A small subset of extremely common conversational connectors (e.g., 'Va bene', 'Grazie mille', 'Per favore') occur frequently enough to warrant Global mapping. The system should support a small **Global Core Phrase** dictionary for these 50-100 high-frequency expressions to prevent tedious repetition, while keeping the other 4,000+ phrases scenario-bound.
