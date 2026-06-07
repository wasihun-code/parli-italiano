# Parla Italiano: Curriculum Data Distribution Audit

## 1. Global Metrics (116 Scenarios)

| Metric | Vocabulary | Phrases | Sentences | Total Items |
| :--- | :--- | :--- | :--- | :--- |
| **Average** | 241.5 | 39.2 | 39.9 | 320.5 |
| **Median** | 240.5 | 40.0 | 40.0 | 320.5 |
| **Min** | 124 | 20 | 20 | 187 |
| **Max** | 375 | 44 | 48 | 455 |

## 2. Top 10 Largest Scenarios (High Cognitive Load)

1.  **culture/local_history**: 455 items
2.  **workstudy/coworking_space**: 442 items
3.  **daily_life/talking_to_a_neighbor**: 436 items
4.  **culture/italian_customs**: 435 items
5.  **social/apologizing**: 431 items
6.  **workstudy/job_interview**: 429 items
7.  **culture/guided_tour**: 421 items
8.  **daily_life/at_the_library**: 420 items
9.  **social/compliments**: 402 items
10. **health/pharmacy_symptoms**: 400 items

## 3. Top 10 Smallest Scenarios (Entry Level)

1.  **miscellaneous/police_report**: 187 items
2.  **tech/online_booking**: 198 items
3.  **adjectives/parole_per_descrivere**: 204 items
4.  **dining/paying_the_bill**: 211 items
5.  **dining/ordering_coffee**: 223 items
6.  **shopping/souvenir_shop**: 224 items
7.  **daily_life/at_the_post_office**: 224 items
8.  **workstudy/university_class**: 226 items
9.  **dining/breakfast_bar**: 227 items
10. **dining/food_allergies**: 242 items

## 4. Distribution Histogram (Total Items)

```text
100-200: ## (2)
200-300: ##################################### (37)
300-400: ################################################################### (67)
400-500: ########## (10)
```

## 5. Case Study: Apartment Key Pickup

**Apartment Key Pickup** (accommodation/apartment_key_pickup) has:
- Vocabulary: 291
- Phrases: 40
- Sentences: 40
- **Total: 371**

**Conclusion:** Apartment Key Pickup is **slightly above average** (371 vs 320.5 mean) but falls well within the standard 300-400 item cluster (which contains 58% of all scenarios). It is representative of the "Standard Gold Scenario" density.

## 6. Audit Findings

1.  **Uniformity:** The median of 40 phrases and 40 sentences across almost all scenarios suggests the `linguistic_extractor.py` or the `Agent 1/2` conversation generation has hard constraints or biases towards these numbers.
2.  **Vocabulary Variance:** The primary source of load variance is vocabulary count (Min 124, Max 375). 
3.  **Cognitive Overload:** 92% of scenarios contain more than 250 total items. When divided into 6 lessons, this results in an average of **~40 vocabulary words per lesson**, plus 6-7 phrases and 6-7 sentences.
4.  **Scale Issue:** The "Local History" scenario (455 items) requires a learner to memorize 62 words and 14 syntactic structures per mini-lesson.
