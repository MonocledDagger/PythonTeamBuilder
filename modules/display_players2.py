def display_players(players):
    print("{:<20} {:<10} {:<9} {:<6} {:<8}".format("PLAYER", "POSITION", "AT BATS", "HITS", "AVERAGE"))#Prints formatted headers
    
    for entry in players.values():  # Prints values
        try:
            hits = entry['hits']
            atbats = entry['atbats']
            average = hits / atbats
        except ZeroDivisionError: # Can't divide by zero
            average = 0
        print("{:<20} {:<10} {:<9} {:<6} {:<8.3f}".format(entry['name'], entry['position'], entry['atbats'], entry['hits'], average))


