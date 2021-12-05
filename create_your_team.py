import random

def create_teams(team_players, no_of_teams):
    num_players = len(team_players)

    if no_of_teams > num_players:
        return "Not enough players to create teams"

    teams = {}
    for i in range(no_of_teams):
        teams[f"Team {i+1}"] = []

    while len(team_players) > 0:
        for team in teams:
            if len(team_players) > 0:
                player = random.choice(team_players)
                teams[team].append(player)
                team_players.remove(player)

    return teams

def display_teams(teams):
    for team in teams:
        print_team = ", ".join(teams[team])
        print(f"{team}: {print_team}")

team_players = input("Please state the name of all the players, serperated by a comma: ").split(",")
no_of_teams = int(input("Please state the number of teams needed: "))
teams = create_teams(team_players,no_of_teams)
display_teams(teams)
