import json
import os

scenario_id = 29
scenario_slug = "dining/ordering_pizza"

def create_choice(text, english, is_correct=True):
    return {
        "text": text,
        "english": english,
        "isCorrect": is_correct
    }

def generate_distractors(text):
    # Simple length-matched distractors for pizza context
    # In a real scenario, these would be more carefully crafted
    length = len(text)
    if "margherita" in text.lower():
        return [
            "Prendo una pizza ai funghi, per favore.",
            "Vorrei una pizza quattro formaggi."
        ]
    if "bufala" in text.lower():
        return [
            "Con mozzarella normale, grazie.",
            "Senza mozzarella, solo pomodoro."
        ]
    if "birra" in text.lower():
        return [
            "Un bicchiere di acqua naturale.",
            "Una bottiglia di vino rosso."
        ]
    if "senza glutine" in text.lower():
        return [
            "Con impasto integrale, grazie.",
            "Vorrei l'impasto tradizionale."
        ]
    if "asporto" in text.lower():
        return [
            "Mangiamo qui al tavolo, grazie.",
            "Per consumazione sul posto."
        ]
    # Default distractors if no specific match
    return [
        "Sì, va bene così, grazie.",
        "No, preferisco qualcos'altro."
    ]

def add_message(messages, role, text, english, learner_response=None):
    msg_id = f"m{len(messages) + 1}"
    msg = {
        "id": msg_id,
        "role": role,
        "text": text,
        "english": english
    }
    if learner_response:
        correct_text, correct_eng = learner_response
        distractors = generate_distractors(correct_text)
        msg["choices"] = [
            create_choice(correct_text, correct_eng, True),
            create_choice(distractors[0], "Distractor 1", False),
            create_choice(distractors[1], "Distractor 2", False)
        ]
    messages.append(msg)

# Conversation 1: Classic Margherita Order
conv1_messages = []
add_message(conv1_messages, "host", "Buonasera! Benvenuti. Volete vedere il menu?", "Good evening! Welcome. Do you want to see the menu?", 
            ("Sì, grazie. Vorrei ordinare una pizza.", "Yes, thank you. I would like to order a pizza."))
add_message(conv1_messages, "host", "Certo. Quale pizza preferite?", "Of course. Which pizza do you prefer?",
            ("Prendo una margherita classica, per favore.", "I'll have a classic margherita, please."))
add_message(conv1_messages, "host", "Ottimo. La margherita è la nostra specialità. La vuole con mozzarella di bufala?", "Excellent. The margherita is our specialty. Do you want it with buffalo mozzarella?",
            ("Sì, con mozzarella di bufala fresca.", "Yes, with fresh buffalo mozzarella."))
add_message(conv1_messages, "host", "Va bene. Desidera un formato particolare? Abbiamo piccola o media.", "Fine. Do you want a particular size? We have small or medium.",
            ("Una pizza media è perfetta per me.", "A medium pizza is perfect for me."))
add_message(conv1_messages, "host", "Perfetto. Vuole aggiungere del basilico fresco sopra?", "Perfect. Do you want to add some fresh basil on top?",
            ("Sì, molto basilico, grazie.", "Yes, lots of basil, thank you."))
add_message(conv1_messages, "host", "D'accordo. Da bere cosa desidera?", "Agreed. What would you like to drink?",
            ("Un bicchiere di vino rosso della casa.", "A glass of house red wine."))
add_message(conv1_messages, "host", "Ottima scelta. La pizza sarà pronta in dieci minuti. Il forno è a legna.", "Excellent choice. The pizza will be ready in ten minutes. The oven is wood-fired.",
            ("Grazie mille. Si sente già il profumo!", "Thanks a lot. I can already smell it!"))
add_message(conv1_messages, "host", "Ecco la sua pizza. Buon appetito!", "Here is your pizza. Enjoy your meal!",
            ("Grazie! Posso avere anche dell'olio piccante?", "Thanks! Can I also have some spicy oil?"))
add_message(conv1_messages, "host", "Certamente, ecco l'olio. Attenzione, è molto forte!", "Certainly, here is the oil. Careful, it is very strong!",
            ("Grazie per l'avvertimento, ne metterò solo un filo.", "Thanks for the warning, I'll only put a drop."))
add_message(conv1_messages, "host", "Perfetto. Serve altro?", "Perfect. Do you need anything else?",
            ("No, va bene così. Grazie di tutto.", "No, it's fine like this. Thanks for everything."))

# Conversation 2: Custom Toppings
conv2_messages = []
add_message(conv2_messages, "host", "Ciao! Cosa vi porto stasera?", "Hi! What can I bring you tonight?",
            ("Vorrei una pizza personalizzata con vari ingredienti.", "I would like a customized pizza with various ingredients."))
add_message(conv2_messages, "host", "Certo! Qual è la base? Pomodoro e mozzarella?", "Sure! What is the base? Tomato and mozzarella?",
            ("Sì, base margherita ma vorrei aggiungere dei funghi.", "Yes, margherita base but I'd like to add some mushrooms."))
add_message(conv2_messages, "host", "Funghi freschi o sott'olio?", "Fresh mushrooms or in oil?",
            ("Funghi freschi, per favore.", "Fresh mushrooms, please."))
add_message(conv2_messages, "host", "Ottimo. Altri ingredienti? Abbiamo prosciutto, olive, carciofi...", "Excellent. Other ingredients? We have ham, olives, artichokes...",
            ("Aggiunga anche del prosciutto crudo, ma a crudo.", "Add some raw ham too, but put it on raw."))
add_message(conv2_messages, "host", "Va bene, il crudo lo mettiamo dopo la cottura. Altro?", "Fine, we'll put the raw ham on after cooking. Anything else?",
            ("Sì, vorrei anche delle olive nere e dei carciofi.", "Yes, I would also like some black olives and artichokes."))
add_message(conv2_messages, "host", "D'accordo. Una pizza molto ricca! Quale formato?", "Agreed. A very rich pizza! Which size?",
            ("La vorrei grande, ho molta fame.", "I would like it large, I'm very hungry."))
add_message(conv2_messages, "host", "Perfetto. E per l'impasto? Abbiamo anche quello integrale.", "Perfect. And for the dough? We also have whole wheat.",
            ("No, preferisco l'impasto tradizionale bianco.", "No, I prefer the traditional white dough."))
add_message(conv2_messages, "host", "Va bene. Da bere?", "Fine. To drink?",
            ("Una birra alla spina media, grazie.", "A medium draft beer, thank you."))
add_message(conv2_messages, "host", "Arriva subito. Ecco la birra.", "Coming right up. Here is the beer.",
            ("Grazie. Quanto tempo devo aspettare per la pizza?", "Thanks. How long do I have to wait for the pizza?"))
add_message(conv2_messages, "host", "Circa quindici minuti, il locale è pieno.", "About fifteen minutes, the place is full.",
            ("Nessun problema, aspetto volentieri.", "No problem, I'll gladly wait."))

# Conversation 3: Takeout Call
conv3_messages = []
add_message(conv3_messages, "host", "Pronto, Pizzeria da Mario. Dica pure.", "Hello, Mario's Pizzeria. Go ahead.",
            ("Buonasera, vorrei ordinare due pizze da asporto.", "Good evening, I'd like to order two pizzas for takeout."))
add_message(conv3_messages, "host", "Certo, quali pizze desidera?", "Sure, which pizzas would you like?",
            ("Una marinara e una quattro formaggi, per favore.", "A marinara and a four cheese, please."))
add_message(conv3_messages, "host", "La marinara con molto aglio o poco?", "The marinara with lots of garlic or a little?",
            ("Con molto aglio e un po' di origano.", "With lots of garlic and a bit of oregano."))
add_message(conv3_messages, "host", "Va bene. E per la quattro formaggi? Formato normale?", "Fine. And for the four cheese? Normal size?",
            ("Sì, formato normale per entrambe.", "Yes, normal size for both."))
add_message(conv3_messages, "host", "D'accordo. A che ora passa a ritirarle?", "Agreed. What time are you coming to pick them up?",
            ("Tra venti minuti circa. Va bene?", "In about twenty minutes. Is that okay?"))
add_message(conv3_messages, "host", "Sì, per le otto sono pronte. Il suo nome?", "Yes, they'll be ready by eight. Your name?",
            ("Mi chiamo Marco Rossi.", "My name is Marco Rossi."))
add_message(conv3_messages, "host", "Va bene Marco. Vuole aggiungere delle bibite?", "Fine Marco. Do you want to add some drinks?",
            ("Sì, due lattine di coca cola fredde.", "Yes, two cold cans of coke."))
add_message(conv3_messages, "host", "Perfetto. Il totale è ventidue euro.", "Perfect. The total is twenty-two euros.",
            ("Posso pagare con la carta quando arrivo?", "Can I pay by card when I arrive?"))
add_message(conv3_messages, "host", "Sì, accettiamo tutte le carte. A dopo!", "Yes, we accept all cards. See you later!",
            ("Grazie mille, a dopo. Arrivederci.", "Thanks a lot, see you later. Goodbye."))
add_message(conv3_messages, "host", "Arrivederci!", "Goodbye!",
            ("Arrivederci e buona serata.", "Goodbye and have a good evening."))

# Conversation 4: Gluten Free Request
conv4_messages = []
add_message(conv4_messages, "host", "Buongiorno! Benvenuti. Avete prenotato?", "Good morning! Welcome. Have you booked?",
            ("Sì, ho una prenotazione per due a nome Bianchi.", "Yes, I have a reservation for two under the name Bianchi."))
add_message(conv4_messages, "host", "Prego, accomodatevi a questo tavolo. Volete il menu?", "Please, sit at this table. Do you want the menu?",
            ("Sì, grazie. Ma volevo chiedere: avete l'impasto senza glutine?", "Yes, thank you. But I wanted to ask: do you have gluten-free dough?"))
add_message(conv4_messages, "host", "Certamente. Abbiamo un'area dedicata per evitare contaminazioni.", "Certainly. We have a dedicated area to avoid contamination.",
            ("Ottimo, è molto importante per me. Grazie.", "Excellent, it's very important for me. Thanks."))
add_message(conv4_messages, "host", "Di nulla. Quale pizza senza glutine desidera?", "You're welcome. Which gluten-free pizza would you like?",
            ("Vorrei una pizza vegetariana senza glutine.", "I would like a gluten-free vegetarian pizza."))
add_message(conv4_messages, "host", "Va bene. La vuole con verdure grigliate o fresche?", "Fine. Do you want it with grilled or fresh vegetables?",
            ("Verdure grigliate, per favore.", "Grilled vegetables, please."))
add_message(conv4_messages, "host", "D'accordo. Altro sopra? Magari un po' di scaglie di parmigiano?", "Agreed. Anything else on top? Maybe some parmesan shavings?",
            ("Sì, ottima idea! Aggiunga pure il parmigiano.", "Yes, great idea! Go ahead and add the parmesan."))
add_message(conv4_messages, "host", "Perfetto. Da bere cosa vi porto?", "Perfect. What can I bring you to drink?",
            ("Avete anche la birra senza glutine?", "Do you also have gluten-free beer?"))
add_message(conv4_messages, "host", "Sì, ne abbiamo una in bottiglia molto buona.", "Yes, we have a very good bottled one.",
            ("Allora prendo quella e un'acqua naturale.", "Then I'll have that and a still water."))
add_message(conv4_messages, "host", "Benissimo. La pizza arriverà tra poco.", "Very well. The pizza will arrive shortly.",
            ("Grazie mille per l'attenzione.", "Thanks a lot for the attention."))
add_message(conv4_messages, "host", "È un piacere. Buon appetito quando arriva!", "It's a pleasure. Enjoy your meal when it arrives!",
            ("Grazie, non vedo l'ora di provarla.", "Thanks, I can't wait to try it."))

conversations = [
    {
        "id": "classic_margherita_order",
        "title": "Classic Margherita Order",
        "description": "Order a traditional pizza margherita with buffalo mozzarella.",
        "messages": conv1_messages
    },
    {
        "id": "custom_toppings",
        "title": "Custom Toppings",
        "description": "Create your own pizza with specific ingredients like mushrooms and ham.",
        "messages": conv2_messages
    },
    {
        "id": "takeout_call",
        "title": "Takeout Call",
        "description": "Order pizzas by phone for collection.",
        "messages": conv3_messages
    },
    {
        "id": "gluten_free_request",
        "title": "Gluten Free Request",
        "description": "Ask for gluten-free options and order a vegetarian pizza.",
        "messages": conv4_messages
    }
]

output = {
    "scenarioId": scenario_id,
    "conversations": conversations
}

with open("src/data/exports/dining/ordering_pizza/conversations.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print("Generated conversations.json successfully.")
