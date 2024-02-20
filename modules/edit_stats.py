from .print_players import print_players #Enumerates Players
from .positive_checker import zero_checker #Checks if number is less than 0
from .positive_checker import positive_checker #Checks if number is less than 1
from .pickle_functions import save_pickle

def edit_stats(players):
    print("")

    print_players(players)

    print("")
    
    edit_number = positive_checker(int(input("Please Enter INDEX of Player You Wish To Edit: ")))
    edit_string= str(edit_number)
    new_edit_name="Player "+edit_string
        
    if 1 <= edit_number <= len(players):
    

        print(f"{players[new_edit_name]['name']} Chosen")
                
        new_atbat = zero_checker(int(input("Please Enter Number of times at bat: ")))
                
                
        new_hits = zero_checker(int(input("Please Enter Number of Hits: ")))
                

                    
        while new_hits > new_atbat:#Hits to Bat Checker
            print("Hits Cannot be more than times at bat")
            new_hits = zero_checker(int(input("Please Enter Number of Hits: ")))

                

        try:
            players[new_edit_name]['atbats'] = new_atbat #Assign new atbat
            players[new_edit_name]['hits'] = new_hits #Assign new Hits
            save_pickle(players, 'player_data.pkl') # Write the updated data back to the dictionary
            print("Player Stats Changed")
        except:
            print("Error Encountered, Player Stats Unchanged")
            
    else:
        print("Invalid entry index. Please try again.")     
            