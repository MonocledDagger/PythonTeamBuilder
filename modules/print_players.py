def print_players(players):
    for i, player in enumerate(players.values(), start=1):#Prints and numbers players
        print(f"{i} {player['name']}")