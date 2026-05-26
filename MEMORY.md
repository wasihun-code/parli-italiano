# MEMORY.md

## Completed Categories
- accommodation ✅
- daily_life ✅
- dining ✅
- travel ✅
- shopping ✅
- culture ✅

## Completed Scenarios
- at_the_bank ✅ (s36, daily_life)
- at_the_gym ✅ (s32, daily_life)
- at_the_library ✅ (s38, daily_life)
- at_the_post_office ✅ (s41, daily_life)
- haircut ✅ (s37, daily_life)
- household_repair ✅ (s39, daily_life)
- laundry_machine ✅ (s33, daily_life)
- making_an_appointment ✅ (s40, daily_life)
- talking_to_a_neighbor ✅ (s35, daily_life)
- weather_small_talk ✅ (s34, daily_life)
- apartment_key_pickup ✅ (s22, accommodation)
- asking_for_towels ✅ (s23, accommodation)
- breakfast_at_hotel ✅ (s24, accommodation)
- extending_stay ✅ (s25, accommodation)
- hostel_dorm ✅ (s26, accommodation)
- hotel_check_in ✅ (s27, accommodation)
- hotel_check_out ✅ (s28, accommodation)
- laundry_service ✅ (s29, accommodation)
- room_problem ✅ (s30, accommodation)
- wi_fi_at_hotel ✅ (s31, accommodation)
- bakery ✅ (validated, dining)
- breakfast_bar ✅ (validated, dining)
- cooking_class ✅ (upgraded, dining)
- food_allergies ✅ (upgraded, dining)
- gelato_shop ✅ (upgraded, dining)
- market_lunch ✅ (upgraded, dining)
- ordering_coffee ✅ (validated, dining)
- ordering_pasta ✅ (upgraded, dining)
- ordering_pizza ✅ (validated, dining)
- paying_the_bill ✅ (validated, dining)
- restaurant_reservation ✅ (validated, dining)
- street_food ✅ (validated, dining)
- vegetarian_meal ✅ (validated, dining)
- wine_bar ✅ (validated, dining)
- airport_arrival ✅ (upgraded, travel)
- asking_directions ✅ (validated, travel)
- baggage_claim ✅ (upgraded, travel)
- bike_rental ✅ (upgraded, travel)
- bus_ticket ✅ (upgraded, travel)
- buying_ferry_tickets ✅ (validated, travel)
- gas_station ✅ (validated, travel)
- lost_in_a_city ✅ (validated, travel)
- metro_directions ✅ (upgraded, travel)
- parking ✅ (validated, travel)
- passport_control ✅ (upgraded, travel)
- renting_a_car ✅ (validated, travel)
- taxi_from_airport ✅ (upgraded, travel)
- train_platform ✅ (upgraded, travel)
- train_ticket ✅ (upgraded, travel)
- travel_emergency ✅ (validated, travel)
- bookstore ✅ (validated, shopping)
- clothing_store ✅ (upgraded, shopping)
- electronics_store ✅ (upgraded, shopping)
- grocery_store ✅ (upgraded, shopping)
- outdoor_market ✅ (upgraded, shopping)
- paying_by_card ✅ (validated, shopping)
- pharmacy_purchase ✅ (upgraded, shopping)
- returning_an_item ✅ (validated, shopping)
- shoe_store ✅ (upgraded, shopping)
- souvenir_shop ✅ (upgraded, shopping)
- church_visit ✅ (validated, culture)
- festival ✅ (upgraded, culture)
- historic_site ✅ (validated, culture)
- italian_customs ✅ (validated, culture)
- live_music ✅ (validated, culture)
- local_history ✅ (validated, culture)
- museum_tickets ✅ (validated, culture)
- sports_match ✅ (validated, culture)
- theater_evening ✅ (validated, culture)
- guided_tour ✅ (upgraded, culture)
- cinema_tickets ✅ (upgraded, culture)
- art_gallery ✅ (upgraded, culture)

## Categories Requiring Audit
- health (undersized phrases/sentences)
- social (undersized phrases/sentences)

## Scenarios Requiring Upgrade (Health)
- buying_medicine
- dental_problem
- doctor_appointment
- emergency_room
- pharmacy_symptoms

## Scenarios Requiring Upgrade (Social)
- apologizing
- at_a_party
- birthday_wishes
- compliments
- introducing_yourself
- inviting_a_friend
- making_plans
- phone_call
- saying_goodbye
- texting_a_friend

## Known Quality Problems
- missing four-part feedback in older datasets (culture, workstudy, etc.)
- undersized datasets in older scenarios (culture, workstudy, etc.)

## Important Architectural Decisions
- sentence stage should feel spoken
- all datasets require bidirectional support
- choicesItalian + choicesEnglish required
- feedback must exist in both languages

## Agent Lessons Learned
- shorter spoken interactions produce better realism
- mini-dialogue sentence structures work best
- emotional realism improves immersion
