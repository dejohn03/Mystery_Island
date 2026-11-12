import game

def run():
    game.start_game()
    
    while True:
        if game.PLAYERS_STATUS.get("game_over"):
            if game.PLAYERS_STATUS.get("won"):
                print("\nCongratulations on winning!")
            else:
                print("\nBetter luck next time!")
            
            replay = input("\nWould you like to play again? (y/n): ").strip().lower()
            if replay == 'y':
                user_name = game.validate_user_name()
                game.reset_game_state(user_name)
                continue
            else:
                print("Thanks for playing The Lost Lighthouse!")
                break

        choice = game.display_menu()

        if choice == 1:
            print(game.explore())
            loc_key = game.PLAYERS_STATUS['current_location']
            if game.ISLAND_MAP[loc_key].get('items'):
                pickup = input("Would you like to collect visible items? (y/n): ").strip().lower()
                if pickup == 'y':
                    print(game.pick_up_item())

        elif choice == 2:
            print(game.list_locations())
            try:
                target_id = int(input("Enter location number to move to (1-5): ").strip())
                print(game.move_player(target_id))
            except ValueError:
                print("Invalid entry. Please enter a valid location number. Energy was not consumed.")

        elif choice == 3:
            print(game.check_inventory())

        elif choice == 4:
            print(game.check_energy())

        elif choice == 5:
            print("Exiting game. Goodbye!")
            break

if __name__ == "__main__":
    run()