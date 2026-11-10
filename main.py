import game

def run_game():
    print("Welcome to Mystery Island")

    players_name = input("Enter your user name: ")

    players_details = {
        "name": players_name, 
        "energy": 5,
        "location": "beach",
        "inventory": []
    }

    print(f"\nWelcome {players_name}")

    for key, value in players_details.items():
        print(f"{key} = {value}")

    while True:
        game.main_menu()
        players_choice = input("Enter user choice: ").strip()

        
        if players_choice == "1":
            game.explore_location(players_details)
        elif players_choice == "2":
            game.travel(players_details)
        elif players_choice == "3":
            game.view_inventory(players_details)
        elif players_choice == "4":
            game.view_map(players_details)
        elif players_choice == "5":
            game.view_status(players_details)
        elif players_choice == "6":    
            print("\nThanks for playing! Goodbye...")
            break
        else:
            print("Invalid input. Please choose an option from 1 to 6.")


if __name__ == "__main__":
    run_game()

