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
        "items": ["wild fruits", "hidden wooden box", "sharp stone", "snakes","hiddden pits"],
        "connections": ["beach", "cave","oldbridge" ]
    },
    "cave": {
        "description": "A dark, echoey cavern with glowing mushrooms.",
        "items": ["glowing mushroom", "old coin", "rope"],
        "connections": ["beach", "lighthouse", "oldbridge"]
},
    "oldbridge": {
        "description": "A breezy, steep peak overlooking the entire island.",
        "items": ["crystal", "wild berries", "lantern"],
        "connections": ["jungle", "lighthouse", "oldbridge"]
    },
    "lighthouse":{
        "description": "A building that contains beacon(a powerful light)",
        "items": ["beacon mechanism", "a recscus signal", "am old logbook"],
        "connections": ["oldbridge", "beach"]
    }
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