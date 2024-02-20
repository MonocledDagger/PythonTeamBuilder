from .print_players import print_players #Displays players
from .pickle_functions import save_pickle
from .positive_checker import positive_checker #Checks if number is less than 1
def edit_position(players):
    positions = ["C", "1B", "2B", "3B", "SS","LF", "CF","RF", "P" ]
            
    print("")

    print_players(players)

    print("")
    
    edit_number = positive_checker(int(input("Please Enter INDEX of Player You Wish To Edit: ")))
    edit_string= str(edit_number) #It breaks if I don't do this
    new_edit_name="Player "+edit_string
        
    if new_edit_name in players:
        
        new_position = input("Please enter a new position for the player: ").upper()

        while new_position not in positions:#Position checker
            new_position = input("Please Enter A Valid Position: ").upper()

        try:
            players[new_edit_name]['position'] = new_position  # Update the player's position in the player list
            save_pickle(players, 'player_data.pkl') # Write the updated data back to the dictionary
            print("Player Position Changed")
        except Exception as e:
            print(f"Error Encountered: {e}. Player Position Unchanged")
    else:
        print("Invalid entry index. Please try again.") 