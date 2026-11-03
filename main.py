def main_menu():
    print(f"""
{"=" * 30}
 WELCOME TO  MYSTERY_ISLAND
{"=" * 30}
    
1. Explore current location
2. travel tgo another location
3. View inventory
4. View island map
5. View player status
6. Quit adventure                                                  
""")
    
def run_game():
    while True:
        print("Welcome to Mystery Island")
        players_name = input("Enter your user name: ")
        print(f"""
Welcome {players_name}
""")
        players_details = {
        "energy": 5,
        "location": "beach",
        "inventory": []
        }

        for key, value in players_details.items():
            print(f"{key} = {value}")

        main_menu()

        players_choice = input("Enter user choice: ").strip()

        

        if players_choice == "6":
            print("Good bye...")
            break



if __name__ == "__main__":
    run_game()