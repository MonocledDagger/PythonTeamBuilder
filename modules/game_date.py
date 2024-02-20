from datetime import date, datetime
def game_date():    
    currentDate= date.today() #Get current date
    
    try: 
        nextGame=input("When is the Next Game?(YYYY-MM-DD): ") #Get next game date
        parsedGame=datetime.strptime(nextGame, "%Y-%m-%d").date() #Converts string input to date
        gameSpan =parsedGame-currentDate
    
        print(f"TODAY'S DATE: {currentDate}")
        print(f"NEXT GAME:{parsedGame}")
    
        if gameSpan.days<1:
            print("")
        else:
            print(f"DAYS UNTIL NEXT GAME: {gameSpan.days}") #Says how many days to next game
    except:
        print("Invalid Input")
