from modules import display_players2, add_player, delete_player, move_players,edit_position, edit_stats,game_date,pickle_functions

#I modulized this. The commands are all modules now

#Command Modules display_players2, add_player, delete_player, move_players,edit_position, edit_stats are for the commands

#game_date module is for Getting and calculating the date and next game

#Pickle functions module is for loading, creating and saving pickles

#Positive checker module is for checking inputs to see if they're above 1 (Or above 0 if using zero_checker), it's used in the command modules
def main():

    exit= False #This is for the main while loop
    
    game_date.game_date()
 

 #Command List            
    print("")
    print("1 - Display Lineup")
    print("2 - Add Player")
    print("3 - Remove Player")
    print("4 - Move Player")
    print("5 - Edit Player Position")
    print("6 - Edit Player Stats")
    print("7 - Exit Program")

    while exit == False:
        try:
            
            players = pickle_functions.load_pickle("player_data.pkl") #Updates players list when you return here, also creates pickle if there isn't one
            #print(players) This is for testing
        except:
            print("Error Loading Pickle")
            break
        
        print("")
        
        try: #Pick Command to Use
            command = int(input("Please Input Command Number: ")) 
        except ValueError:
            print("Please Enter a Valid Number")
            command = int(input("Please Input Command Number: ")) 
                  
        try:   
            if command == 1: #DISPLAY command displays player data
                
                display_players2.display_players(players)
            
            elif command == 2: #ADD command adds a new player
                
                add_player.add_player()
                
            elif command == 3: #DELETE command removes a player
                
                delete_player.delete_player(players)
            
            elif command == 4:#MOVE command moves a player to another position
                
                move_players.move_players(players)
                
            elif command == 5:#EDIT POSITION command changes position of player
                
                edit_position.edit_position(players) 
                
            elif command == 6:#EDIT STATS command changes at bats and hits
                
                edit_stats.edit_stats(players)   
                
            elif command == 7:#EXIT command stops program
                print("Goodbye!")
                exit = True
                
            else:#Reprint commands if invalid command entered
                print("Please Input valid number(1-7)")
                print("1 - Display Lineup")
                print("2 - Add Player")
                print("3 - Remove Player")
                print("4 - Move Player")
                print("5 - Edit Player Position")
                print("6 - Edit Player Stats")
                print("7 - Exit Program")
                
        except:#Not sure how anyone would get here but I think I did once 
            print("Please Input valid number(1-7)")
            print("1 - Display Lineup")
            print("2 - Add Player")
            print("3 - Remove Player")
            print("4 - Move Player")
            print("5 - Edit Player Position")
            print("6 - Edit Player Stats")
            print("7 - Exit Program")
            
            
if __name__ == '__main__': #main 
    main()