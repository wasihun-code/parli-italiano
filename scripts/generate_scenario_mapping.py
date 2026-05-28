import os
import re

canonical = [
    (1, 'Travel', 'Airport Arrival'), (2, 'Travel', 'Passport Control'), (3, 'Travel', 'Baggage Claim'),
    (4, 'Travel', 'Taxi From Airport'), (5, 'Travel', 'Train Ticket'), (6, 'Travel', 'Train Platform'),
    (7, 'Travel', 'Bus Ticket'), (8, 'Travel', 'Metro Directions'), (9, 'Travel', 'Asking Directions'),
    (10, 'Travel', 'Renting a Car'), (11, 'Travel', 'Gas Station'), (12, 'Travel', 'Parking'),
    (13, 'Travel', 'Lost in a City'), (14, 'Travel', 'Buying Ferry Tickets'), (15, 'Travel', 'Bike Rental'),
    (16, 'Travel', 'Travel Emergency'), (17, 'Accommodation', 'Hotel Check-In'), (18, 'Accommodation', 'Hotel Check-Out'),
    (19, 'Accommodation', 'Room Problem'), (20, 'Accommodation', 'Asking for Towels'), (21, 'Accommodation', 'Breakfast at Hotel'),
    (22, 'Accommodation', 'Apartment Key Pickup'), (23, 'Accommodation', 'Wi-Fi at Hotel'), (24, 'Accommodation', 'Laundry Service'),
    (25, 'Accommodation', 'Extending Stay'), (26, 'Accommodation', 'Hostel Dorm'), (27, 'Dining', 'Restaurant Reservation'),
    (28, 'Dining', 'Ordering Coffee'), (29, 'Dining', 'Ordering Pizza'), (30, 'Dining', 'Ordering Pasta'),
    (31, 'Dining', 'Gelato Shop'), (32, 'Dining', 'Paying the Bill'), (33, 'Dining', 'Food Allergies'),
    (34, 'Dining', 'Vegetarian Meal'), (35, 'Dining', 'Wine Bar'), (36, 'Dining', 'Bakery'),
    (37, 'Dining', 'Street Food'), (38, 'Dining', 'Breakfast Bar'), (39, 'Dining', 'Cooking Class'),
    (40, 'Dining', 'Market Lunch'), (41, 'Shopping', 'Clothing Store'), (42, 'Shopping', 'Shoe Store'),
    (43, 'Shopping', 'Grocery Store'), (44, 'Shopping', 'Outdoor Market'), (45, 'Shopping', 'Pharmacy Purchase'),
    (46, 'Shopping', 'Souvenir Shop'), (47, 'Shopping', 'Electronics Store'), (48, 'Shopping', 'Bookstore'),
    (49, 'Shopping', 'Returning an Item'), (50, 'Shopping', 'Paying by Card'), (51, 'Daily Life', 'At the Bank'),
    (52, 'Daily Life', 'At the Post Office'), (53, 'Daily Life', 'Haircut'), (54, 'Daily Life', 'Laundry Machine'),
    (55, 'Daily Life', 'Weather Small Talk'), (56, 'Daily Life', 'Making an Appointment'), (57, 'Daily Life', 'At the Gym'),
    (58, 'Daily Life', 'At the Library'), (59, 'Daily Life', 'Talking to a Neighbor'), (60, 'Daily Life', 'Household Repair'),
    (61, 'WorkStudy', 'First Day at Work'), (62, 'WorkStudy', 'Team Meeting'), (63, 'WorkStudy', 'Asking for Clarification'),
    (64, 'WorkStudy', 'Email Follow-Up'), (65, 'WorkStudy', 'University Class'), (66, 'WorkStudy', 'Language School'),
    (67, 'WorkStudy', 'Job Interview'), (68, 'WorkStudy', 'Coworking Space'), (69, 'WorkStudy', 'Printing Documents'),
    (70, 'WorkStudy', 'Study Group'), (71, 'Social', 'Introducing Yourself'), (72, 'Social', 'Making Plans'),
    (73, 'Social', 'Inviting a Friend'), (74, 'Social', 'At a Party'), (75, 'Social', 'Phone Call'),
    (76, 'Social', 'Texting a Friend'), (77, 'Social', 'Apologizing'), (78, 'Social', 'Compliments'),
    (79, 'Social', 'Birthday Wishes'), (80, 'Social', 'Saying Goodbye'), (81, 'Culture', 'Museum Tickets'),
    (82, 'Culture', 'Church Visit'), (83, 'Culture', 'Cinema Tickets'), (84, 'Culture', 'Theater Evening'),
    (85, 'Culture', 'Live Music'), (86, 'Culture', 'Art Gallery'), (87, 'Culture', 'Guided Tour'),
    (88, 'Culture', 'Historic Site'), (89, 'Culture', 'Festival'), (90, 'Culture', 'Sports Match'),
    (91, 'Culture', 'Italian Customs'), (92, 'Culture', 'Local History'), (93, 'Health', 'Pharmacy Symptoms'),
    (94, 'Health', 'Doctor Appointment'), (95, 'Health', 'Emergency Room'), (96, 'Health', 'Dental Problem'),
    (97, 'Health', 'Buying Medicine'), (98, 'Tech', 'Buying a SIM Card'), (99, 'Tech', 'Wi-Fi Problem'),
    (100, 'Tech', 'Phone Repair'), (101, 'Tech', 'Charging Devices'), (102, 'Tech', 'Using a Map App'),
    (103, 'Tech', 'Video Call'), (104, 'Tech', 'Online Booking'), (105, 'Tech', 'ATM Machine'),
    (106, 'Miscellaneous', 'Police Report'), (107, 'Miscellaneous', 'Asking for Help'), (108, 'Miscellaneous', 'Talking About Money'),
    (109, 'Miscellaneous', 'Time and Dates'), (110, 'Miscellaneous', 'Explaining a Mistake'), (111, 'Animals', 'Animali'),
    (112, 'Verbs_ARE', 'Verbi in -ARE'), (113, 'Verbs_ERE', 'Verbi in -ERE'), (114, 'Verbs_IRE', 'Verbi in -IRE'),
    (115, 'Reflexive_Verbs', 'Verbi Riflessivi'), (116, 'Adjectives', 'Parole per Descrivere')
]

def slugify(t):
    return re.sub(r'[^a-z0-9]+', '_', t.lower()).strip('_')

base_dir = "src/data/exports"
output_file = "src/data/scenarioMapping.ts"

mapping = {}

for s_id, cat, title in canonical:
    cat_slug = slugify(cat)
    if cat_slug == "workstudy": cat_slug = "workstudy" # special case
    if cat_slug == "daily_life": cat_slug = "daily_life" # special case
    
    title_slug = slugify(title)
    # Manual overrides for specific folders
    if s_id == 111: path = "exports/animals/animali"
    elif s_id == 112: path = "exports/verbs/are_verbi_in_are"
    elif s_id == 113: path = "exports/verbs/ere_verbi_in_ere"
    elif s_id == 114: path = "exports/verbs/ire_verbi_in_ire"
    elif s_id == 115: path = "exports/reflexive/verbs_verbi_riflessivi"
    elif s_id == 116: path = "exports/adjectives/parole_per_descrivere"
    else:
        # Check in the category folder
        # Note: some categories might be named differently in exports
        search_cat = cat_slug
        if search_cat == "workstudy": search_cat = "workstudy"
        
        path = os.path.join("exports", search_cat, title_slug)
        if not os.path.exists(os.path.join("src/data", path)):
            # Try workstudy vs work_study
            if search_cat == "workstudy":
                 path = os.path.join("exports", "workstudy", title_slug)
            
            # Final check
            if not os.path.exists(os.path.join("src/data", path)):
                print(f"Warning: Folder not found for s{s_id}: {path} ({title})")
                continue

    mapping[s_id] = path

with open(output_file, "w", encoding="utf-8") as f:
    f.write("export const scenarioMapping: Record<number, string> = {\n")
    for s_id in sorted(mapping.keys()):
        f.write(f"  {s_id}: '{mapping[s_id]}',\n")
    f.write("};\n")

print(f"Generated {output_file} with {len(mapping)} mappings.")
