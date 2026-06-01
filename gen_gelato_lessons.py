
import json

scenario_id = 31
prefix = f"s{scenario_id}"

lessons = [
    {
        "id": "l1",
        "title": "Lesson 1",
        "goal": "Gelato Basics",
        "estimatedDuration": "3 mins",
        "unlockCriteria": "none",
        "nextLesson": "l2",
        "sections": [
            {
                "type": "vocabulary",
                "title": "Learn the Words",
                "description": "Essential greetings and ordering words.",
                "exerciseIds": [f"{prefix}-v18", f"{prefix}-v21", f"{prefix}-v22", f"{prefix}-v29", f"{prefix}-v64", f"{prefix}-v68", f"{prefix}-v169"]
            },
            {
                "type": "phrase",
                "title": "Build the Phrases",
                "description": "Basic ordering phrases.",
                "exerciseIds": [f"{prefix}-p31", f"{prefix}-p40", f"{prefix}-p8"]
            },
            {
                "type": "sentence",
                "title": "Practice the Dialogue",
                "description": "How the host greets you.",
                "exerciseIds": [f"{prefix}-s5", f"{prefix}-s7"]
            },
            {
                "type": "mastery",
                "title": "Mastery Check",
                "description": "Order your first gelato.",
                "exerciseIds": [f"{prefix}-p31"]
            }
        ]
    },
    {
        "id": "l2",
        "title": "Lesson 2",
        "goal": "Flavors",
        "estimatedDuration": "3 mins",
        "unlockCriteria": "complete_previous",
        "nextLesson": "l3",
        "sections": [
            {
                "type": "vocabulary",
                "title": "Learn the Words",
                "description": "Common gelato flavors.",
                "exerciseIds": [f"{prefix}-v31", f"{prefix}-v56", f"{prefix}-v78", f"{prefix}-v38", f"{prefix}-v162", f"{prefix}-v92", f"{prefix}-v148", f"{prefix}-v112", f"{prefix}-v60"]
            },
            {
                "type": "phrase",
                "title": "Build the Phrases",
                "description": "Asking for specific flavors.",
                "exerciseIds": [f"{prefix}-p37", f"{prefix}-p38", f"{prefix}-p26"]
            },
            {
                "type": "sentence",
                "title": "Practice the Dialogue",
                "description": "Discussing flavors with the host.",
                "exerciseIds": [f"{prefix}-s37", f"{prefix}-s21"]
            },
            {
                "type": "mastery",
                "title": "Mastery Check",
                "description": "Pick your flavors.",
                "exerciseIds": [f"{prefix}-p37"]
            }
        ]
    },
    {
        "id": "l3",
        "title": "Lesson 3",
        "goal": "Cone or Cup",
        "estimatedDuration": "3 mins",
        "unlockCriteria": "complete_previous",
        "nextLesson": "l4",
        "sections": [
            {
                "type": "vocabulary",
                "title": "Learn the Words",
                "description": "Choosing how to eat your gelato.",
                "exerciseIds": [f"{prefix}-v33", f"{prefix}-v34", f"{prefix}-v116", f"{prefix}-v133", f"{prefix}-v12"]
            },
            {
                "type": "phrase",
                "title": "Build the Phrases",
                "description": "Cone or cup?",
                "exerciseIds": [f"{prefix}-p39", f"{prefix}-p35", f"{prefix}-p28"]
            },
            {
                "type": "sentence",
                "title": "Practice the Dialogue",
                "description": "Host asking for your preference.",
                "exerciseIds": [f"{prefix}-s8", f"{prefix}-s30"]
            },
            {
                "type": "mastery",
                "title": "Mastery Check",
                "description": "Choose between cono and coppetta.",
                "exerciseIds": [f"{prefix}-p39"]
            }
        ]
    },
    {
        "id": "l4",
        "title": "Lesson 4",
        "goal": "Panna & Toppings",
        "estimatedDuration": "3 mins",
        "unlockCriteria": "complete_previous",
        "nextLesson": "l5",
        "sections": [
            {
                "type": "vocabulary",
                "title": "Learn the Words",
                "description": "Whipped cream and toppings.",
                "exerciseIds": [f"{prefix}-v103", f"{prefix}-v90", f"{prefix}-v62", f"{prefix}-v3", f"{prefix}-v147", f"{prefix}-v107"]
            },
            {
                "type": "phrase",
                "title": "Build the Phrases",
                "description": "Adding extra deliciousness.",
                "exerciseIds": [f"{prefix}-p18", f"{prefix}-p32", f"{prefix}-p15"]
            },
            {
                "type": "sentence",
                "title": "Practice the Dialogue",
                "description": "Host offering toppings.",
                "exerciseIds": [f"{prefix}-s23", f"{prefix}-s11"]
            },
            {
                "type": "mastery",
                "title": "Mastery Check",
                "description": "Request or decline panna.",
                "exerciseIds": [f"{prefix}-p18"]
            }
        ]
    },
    {
        "id": "l5",
        "title": "Lesson 5",
        "goal": "Sizes",
        "estimatedDuration": "3 mins",
        "unlockCriteria": "complete_previous",
        "nextLesson": "l6",
        "sections": [
            {
                "type": "vocabulary",
                "title": "Learn the Words",
                "description": "Sizes for cones and cups.",
                "exerciseIds": [f"{prefix}-v111", f"{prefix}-v82", f"{prefix}-v67", f"{prefix}-v48", f"{prefix}-v87"]
            },
            {
                "type": "phrase",
                "title": "Build the Phrases",
                "description": "Picking a size.",
                "exerciseIds": [f"{prefix}-p34", f"{prefix}-p22", f"{prefix}-p11"]
            },
            {
                "type": "sentence",
                "title": "Practice the Dialogue",
                "description": "Host asking about size.",
                "exerciseIds": [f"{prefix}-s35", f"{prefix}-s25"]
            },
            {
                "type": "mastery",
                "title": "Mastery Check",
                "description": "Specify the size of your order.",
                "exerciseIds": [f"{prefix}-p34"]
            }
        ]
    },
    {
        "id": "l6",
        "title": "Lesson 6",
        "goal": "Groups",
        "estimatedDuration": "3 mins",
        "unlockCriteria": "complete_previous",
        "nextLesson": "none",
        "sections": [
            {
                "type": "vocabulary",
                "title": "Learn the Words",
                "description": "Ordering for others and paying.",
                "exerciseIds": [f"{prefix}-v69", f"{prefix}-v154", f"{prefix}-v73", f"{prefix}-v52", f"{prefix}-v25", f"{prefix}-v100", f"{prefix}-v136"]
            },
            {
                "type": "phrase",
                "title": "Build the Phrases",
                "description": "Group interactions.",
                "exerciseIds": [f"{prefix}-p41", f"{prefix}-p27", f"{prefix}-p5"]
            },
            {
                "type": "sentence",
                "title": "Practice the Dialogue",
                "description": "Finalizing the group order.",
                "exerciseIds": [f"{prefix}-s6", f"{prefix}-s26", f"{prefix}-s16"]
            },
            {
                "type": "mastery",
                "title": "Mastery Check",
                "description": "Finish the transaction.",
                "exerciseIds": [f"{prefix}-p27"]
            }
        ]
    }
]

data = {
    "lessons": lessons
}

with open("src/data/exports/dining/gelato_shop/mini_lessons.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
