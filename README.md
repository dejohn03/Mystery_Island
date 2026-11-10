# Mystery_Island

import random

ISLAND_MAP = {
    "beach":{
        "description": """The ocean stretches endlessly before you. Tall palm trees sway in the wind, while strange birds fly above them. "
        Pieces of your broken ship are scattered along the beach.s""",
        "items": ["shipwreck", "coconut", "Rope","Rusty key","wooden chest","palm trees"],
        "connections": ["jungle", "cave","lighthouse"], 
    },
    "jungle":{
        "description": """The sunlight struggles to pass through the thick leaves.
          The ground is covered with roots, fallen branches, and wet leaves.
          As you walk deeper into the Jungle, you notice that something is watching you. You hear birds calling, 
          monkeys jumping between branches, and strange noises coming from the bushe""",
        "items": ["wild fruits", "hidden wooden box", "sharp stone", "snakes","hiddden pits","medicinal leaves","strong vines", ],
        "connections": ["beach", "cave","oldbridge" ]
    },
    "cave": {
        "description": """The entrance is narrow, and cold air blows from inside. Water drips from the ceiling, creating strange echoes throughout the cave.

        You switch on your light and carefully step inside.
        As you explore deeper, you discover ancient drawings on the walls,
        broken wooden boxes, mysterious symbols, and an old stone door..""",
        "items": ["glowing crystal", "hidden treasure chest", "climblin rope", "ancient stone tablet", "old lantern","ancient key"],
        "connections": ["beach", "lighthouse", "oldbridge"]
},
    "oldbridge": {
        "description": "A breezy, steep peak overlooking the entire island.",
        "items": ["crystal", "wild berries", "lantern"],
        "cave dangers"["deep holes", "falling", "ba]
        "connections": ["jungle", "lighthouse", "oldbridge"]
    },
    "lighthouse":{
        "description": "A building that contains beacon(a powerful light)",
        "items": ["beacon mechanism", "a recscus signal", "am old logbook"],
        "connections": ["oldbridge", "beach"]