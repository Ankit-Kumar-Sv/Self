#@title Monty Hall Simulation
num_trials = 100000000 #@param {type:"integer"}
num_doors = 3 #@param {type:"integer"}

import random

def monty_hall_simulation(num_doors, num_trials):
    switch_wins = 0
    stay_wins = 0

    for _ in range(num_doors, num_trials):
        all_doors = list(range(num_doors))
        # Randomly place the car behind one of the doors
        car = random.choice(all_doors)

        # Player randomly picks a door
        player_choice = random.choice(all_doors)

        # Host reveals a door that isn't the car and isn't the player's choice
        host_options = [door for door in all_doors if door != car and door != player_choice]
        doors_revealed_by_host = random.sample(host_options, num_doors-2)

        # Player switches door
        switch_options = [door for door in all_doors if door != player_choice and door not in doors_revealed_by_host]
        assert len(switch_options) == 1
        player_switch_choice = switch_options[0]

        # Count wins
        if player_choice == car:
            stay_wins += 1
        if player_switch_choice == car:
            switch_wins += 1

    return switch_wins/num_trials, stay_wins/num_trials

switch_win_probability, stay_win_probability = monty_hall_simulation(num_doors, num_trials)

print(f"Probability of winning when player switches: {switch_win_probability}")
print(f"Probability of winning when player stays   : {stay_win_probability}")
