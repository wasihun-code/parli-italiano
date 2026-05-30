# Domain Integrity Rules

## Purpose
Every scenario in Parla Italiano is highly focused on a specific, real-world context (e.g., picking up keys, buying a train ticket). Lexical contamination breaks the immersive experience and confuses learners.

## The Rule
A scenario must have 0% contamination from unrelated domains. 

## Detection
The `scripts/domain_audit.py` script enforces this. For the reference implementation (`apartment_key_pickup`), a strict allowed/forbidden list is used. Future scenarios will implement a similar matrix or utilize an LLM-based verification pass within the certification pipeline.

## Example: Apartment Key Pickup
**ALLOWED CONCEPTS:**
*   apartment (appartamento)
*   host (proprietario)
*   keys (chiavi)
*   intercom (citofono)
*   building (palazzo)
*   address (indirizzo)
*   entrance (portone)

**FORBIDDEN CONCEPTS:**
*   restaurant (ristorante, menu, cameriere)
*   airport (aeroporto, volo, bagaglio)
*   doctor (medico, ospedale, dolore)
*   train (treno, binario, biglietto)
*   coffee (caffè, bar, cappuccino)

## Distractor Purity
Distractors must also adhere to the domain rules. You cannot use "il menu" as a distractor when the user is trying to find an apartment. Distractors should be linguistically plausible alternatives within the SAME physical space or context.
