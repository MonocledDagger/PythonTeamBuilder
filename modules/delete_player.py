from .print_players import print_players
from .pickle_functions import save_pickle

def delete_player(players): 
    print("")
    print_players(players)

            
    del_name = input("Please Enter INDEX of Player to Delete ")
    new_del_name= "Player " + del_name
            
                
    try: #Deletes player, saves to pickle
    
        del players[new_del_name]
        save_pickle(players, 'player_data.pkl') 
        print("Entry deleted successfully.")
    
    except:
        print("Invalid Number")