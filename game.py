import copy

INITIAL_ISLAND_MAP = {
    "beach": {
        "id": 1,
        "name": "beach",
        "info": """A sandy shore strewn with shipwreck debris.You wake up on a beautiful but mysterious island after a terrible storm destroys your ship. "
        "You find yourself lying on soft white sand, with waves gently washing against the shore""",
        "items": ["Rope","Rusty key", "wooden chest"]
    },
    "jungle": {
        "id": 2,
        "name": "jungle",
        "info": "A dense, humid jungle filled with mysterious sounds.",
        "items": ["snakes", "hidden pit","fruils"]
    },
    "cave": {
        "id": 3,
        "name": "cave",
        "info": """A dark, damp cavern.The Cave is the third location on Mystery Island."
        After travelling through the thick Jungle,"
         you discover a dark cave hidden between enormous rocks.""",
        "items": ["Lantern"]
    },
    "old-bridge": {
        "id": 4,
        "name": "old-bridge",
        "info": "A rickety wooden bridge spanning a deep chasm."
        "The Old Bridge is the fourth location on Mystery Island. After escaping the Cave, "
        "you follow a narrow rocky path until you discover an old wooden bridge hanging over a deep valley.",
        "items": ["metal hook","hammer","iron nails"]
    },
    "light-house": {
        "id": 5,
        "name": "light-house",
        "info": "An ancient lighthouse with an unlit beacon."
        "The lighthouse is very old. Its white paint is peeling, its windows are broken, "
        "and its entrance is covered with dust and cobwebs.",
        "items": ["instruction notebook","lighthouse key"]
    }
}

PLAYERS_STATUS = {}
ISLAND_MAP = {}


def reset_game_state(user_name: str = "Player"):
    global PLAYERS_STATUS, ISLAND_MAP
    ISLAND_MAP = copy.deepcopy(INITIAL_ISLAND_MAP)
    PLAYERS_STATUS = {
        "user_name": user_name,
        "energy": 5,
        "current_location": "beach",
        "inventory": [],
        "game_over": False,
        "won": False
    }


def _validate_action() -> tuple[int, str]:
    try:
        raw_input = input("Select Action (1-5): ").strip()
        users_choice = int(raw_input)
        if users_choice not in range(1, 6):
            raise ValueError("Choose a valid option between 1 and 5.")
        return (users_choice, "")
    except ValueError as err:
        return (0, f"Error: {err}")
    except Exception as err:
        return (0, f"Unexpected Error: {err}")


def validate_user_name() -> str:
    while True:
        user_name = input("Enter your username: ").strip()
        if not user_name:
            print("Enter a valid username.")
            continue
        return user_name


def start_game():
    print("=" * 40)
    print("Welcome to The Lost Lighthouse!".center(40))
    print("=" * 40)
    print("""
You have been stranded on a mysterious island after a shipwreck.
Your mission is to explore the island, collect useful items, and find a way
to signal a rescue boat.

Rules of the Game
-----------------
1. Enter your name to begin your adventure.
2. You start at the Beach with 5 energy points.
3. Explore the five locations: Beach, Jungle, Cave, Old Bridge, and Lighthouse.
4. Collect useful items and keep them in your inventory.
5. You need a Rope to cross the Old Bridge.
6. You need a Lantern to light the Lighthouse beacon.
7. Each successful movement costs 1 energy point.
8. Invalid movements do not consume energy.
9. If your energy reaches zero before rescue, you lose.
10. Light the lighthouse beacon to win the game.
""")
    user_name = validate_user_name()
    reset_game_state(user_name)


def display_menu() -> int:
    print(f"\n=========> {PLAYERS_STATUS.get('user_name', 'Unknown Player')} <=========")
    print(f"Current Location : {PLAYERS_STATUS.get('current_location', '').title()}")
    print(f"Remaining Energy : {PLAYERS_STATUS.get('energy', 0)}")
    print(f"Inventory        : {', '.join(PLAYERS_STATUS.get('inventory', [])) or 'Empty'}")
    print("-" * 43)
    print("What would you like to do?")
    print("1. Explore location")
    print("2. Move to another location")
    print("3. Check inventory")
    print("4. Check energy")
    print("5. Quit game")

    while True:
        users_choice, err = _validate_action()
        if err:
            print(err)
            continue
        return users_choice


def explore() -> str:
    loc_key = PLAYERS_STATUS['current_location']
    loc_data = ISLAND_MAP[loc_key]
    items = loc_data.get('items', [])
    item_str = ", ".join(items) if items else "None"
    return (
        f"\n--- Exploring {loc_key.title()} ---\n"
        f"{loc_data.get('info', '')}\n"
        f"Items visible: {item_str}\n"
    )


def pick_up_item() -> str:
    loc_key = PLAYERS_STATUS['current_location']
    items = ISLAND_MAP[loc_key].get('items', [])
    if not items:
        return "There are no items to collect here."

    collected = []
    for item in list(items):
        PLAYERS_STATUS['inventory'].append(item)
        items.remove(item)
        collected.append(item)

    return f"You picked up: {', '.join(collected)}!"


def list_locations() -> str:
    full_list = "\nList of Moveable Locations:\n"
    for location, details in ISLAND_MAP.items():
        tag = " <current location>" if location == PLAYERS_STATUS["current_location"] else ""
        full_list += f"{details['id']}. {location.title()}{tag}\n"
    return full_list


def move_player(location_id: int) -> str:
    if PLAYERS_STATUS.get("game_over"):
        return "The game is already over."

    target_key = None
    for loc_key, details in ISLAND_MAP.items():
        if details["id"] == location_id:
            target_key = loc_key
            break

    if not target_key:
        return "Invalid location selection. Energy was not consumed."

    if target_key == PLAYERS_STATUS["current_location"]:
        return "You are already at this location. Energy was not consumed."

    if target_key == "old-bridge" and "Rope" not in PLAYERS_STATUS["inventory"]:
        return "You cannot cross the Old Bridge without a Rope! Energy was not consumed."

    if target_key == "light-house" and "Lantern" not in PLAYERS_STATUS["inventory"]:
        return "The path to the Lighthouse is too dark. You need a Lantern! Energy was not consumed."

    PLAYERS_STATUS["current_location"] = target_key
    PLAYERS_STATUS["energy"] -= 1

    msg = f"You moved to {target_key.title()}. Energy remaining: {PLAYERS_STATUS['energy']}."

    if target_key == "light-house" and "Lantern" in PLAYERS_STATUS["inventory"]:
        PLAYERS_STATUS["won"] = True
        PLAYERS_STATUS["game_over"] = True
        msg += "\n\n*** VICTORY! You lit the lighthouse beacon and signaled a rescue boat! ***"
        return msg

    if PLAYERS_STATUS["energy"] <= 0:
        PLAYERS_STATUS["game_over"] = True
        msg += "\n\n*** GAME OVER! You ran out of energy before restoring the beacon. ***"

    return msg


def check_inventory() -> str:
    inv = PLAYERS_STATUS.get("inventory", [])
    if inv:
        return f"\nInventory: {', '.join(inv)}"
    return "\nYour inventory is empty."


def check_energy() -> str:
    return f"\nRemaining Energy: {PLAYERS_STATUS.get('energy', 0)} / 5"