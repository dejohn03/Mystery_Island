
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
        "items": ["wild fruits", "hidden wooden box", "sharp stone", "snakes","hiddden pits","medicinal leaves","strong vines"], 
        "connections": ["beach", "cave","oldbridge" ]
    },
    "cave": {
        "description": """The entrance is narrow, and cold air blows from inside. Water drips from the ceiling, creating strange echoes throughout the cave.
        You switch on your light and carefully step inside.
        As you explore deeper, you discover ancient drawings on the walls,
        broken wooden boxes, mysterious symbols, and an old stone door..""",
        "items": ["glowing crystal", "hidden treasure chest", 
        "climblin rope", "ancient stone tablet", "old lantern","ancient key"],
        "cave dangers":["deep holes", "falling", "darkness"],

        "connections": ["beach", "lighthouse", "old bridge"],
    },    

    "old bridge": {
        "description": """The bridge looks very weak. Some of its wooden planks are broken,
        and its ropes are old and damaged. Far below, a river flows between enormous rocks.
        Strong winds blow across the valley, 
        making the bridge swing from side to side.

        You look across the bridge and notice something important: 
        the other side leads towards a mountain path, and beyond that mountain stands the Lighthouse.

        You must find a way to repair or safely cross the bridge before continuing your journey.""",
        "items": ["Wooden planks", "Iron nails", "Hammer","Spare rope","Metal hook","Old map"],
        "old bridge":["broken planks", "weak ropes", "strong winds", "deep valley"],
        "connections": ["jungle", "lighthouse", "oldbridge"]
    },
    "lighthouse":{
        "description": """After successfully crossing the Old Bridge, you follow a rocky mountain
          path until you finally see an enormous lighthouse standing on the edge of the island.
        The lighthouse is very old. Its white paint is peeling, its windows are broken, 
        and its entrance is covered with dust and cobwebs.
        You are excited because this is the place where the rescue boat is supposed to find you.
        As you approach the lighthouse, you notice that its main door is locked. 
        You must explore the building,
        find useful equipment, and activate the lighthouse signal to attract the rescue boat.""",
        "items": ["Lighthouse key", "a recscus signal", "Instruction notebook"],
        "lighthouse dangers" : ["broken staircase", "electical", "locked control room", "power failure"],
        "connections": ["oldbridge", "beach"]
    },
}
def main_menu():
    print(f"""
{"=" * 30}
 WELCOME TO MYSTERY_ISLAND
{"=" * 30}

1. Explore current location
2. Travel to another location
3. View inventory
4. View island map
5. View player status
6. Quit adventure
""")

def explore_location(players_details):
    current_loc = players_details["location"]
    print(f"\n--- Exploring {current_loc.title()} ---")
    print(ISLAND_MAP[current_loc]["description"])

    if players_details["energy"] <= 0:
        print("you are too tired to explore! Rest or travel to find a safe spot.")
        return

    players_details["energy"] -= 1

    available_items = ISLAND_MAP[current_loc]["items"]
    if available_items and random.random() > 0.3: 
        found_item = random.choice(available_items)
        players_details["inventory"].append(found_item)
        print(f"🎉 You found a [{found_item}] and added it to your inventory!")
    else:
        print("You looked around but didn't find anything new.")


def travel(players_details):
    current_loc = players_details["location"]
    possible_destinations = ISLAND_MAP[current_loc]["connections"]
    
    print(f"\nYou are currently at the {current_loc.title()}.")
    print("Where would you like to travel?")

    for index, destination in enumerate(possible_destinations, 1):
        print(f"{index}. {destination.title()}")
    print(f"{len(possible_destinations) + 1}. Cancel and go back")
    
    choice = input("Enter the number of your destination: ").strip()
    
    # Process movement choice
    if choice.isdigit():
        choice_idx = int(choice) - 1
        if 0 <= choice_idx < len(possible_destinations):
            new_location = possible_destinations[choice_idx]
            players_details["location"] = new_location
            print(f"✈️ You traveled through the wilderness and arrived at the {new_location.title()}!")
            
            # Simple mechanic: traveling might restore or use energy, let's say it costs nothing for now
        elif choice_idx == len(possible_destinations):
            print("Travel canceled.")
        else:
            print("Invalid location choice.")
    else:
        print("Please enter a valid number.")


def view_inventory(players_details):
    print(f"\n--- {players_details["name"]}'s Inventory ---")
    if not players_details["inventory"]:
        print("Your inventory is empty.")
    else:
        for item in players_details["inventory"]:
            print(f"- {item}")

def view_map(players_details):
    print(f"\n--- Island Map ---")
    for loc, info in ISLAND_MAP.items():
        prefix = "📌 (You are here) " if loc == players_details["location"] else "📍 "
        connections_str = ", ".join([c.title() for c in info["connections"]])
        print(f"{prefix}{loc.title()}: Connects to -> {connections_str}")

def view_status(players_details):
    print(f"\n--- {players_details['name']}'s Status ---")
    print(f"Energy  : {players_details['energy']} ⚡")
    print(f"Location: {players_details['location'].title()} 📍")
    print(f"Items   : {len(players_details['inventory'])} in backpack 🎒")