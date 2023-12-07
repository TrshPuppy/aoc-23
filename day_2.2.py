# what is the fewest number of cubes of each color that could have
# been in the bag to make the game possible?
# Game power = the fewest number of each cube multiplied
power_sum = 0

# Major game loop:
for i, line in enumerate(input.split(f"\n")):
    # Chop off 'Game X:' portion of string
    chopped_line = line.split(f":")[1]

    # For each round, save the highest cube value seen of ea color:
    round_cubes = [0, 0, 0]  # r, g, b
    game_power = 0

    # Loop through game to get rounds:
    for round in chopped_line.split(f";"):
        impossible = False

        # Loop through round to get colors:
        for cubes in round.split(f","):
            # Break toss into number and color [number, color]
            result = [int(cubes.split(" ")[1]), cubes.split(" ")[2]]

            # Get results for cube colors thrown and save highest number for ea color:
            if result[1] == "red":
                if result[0] > round_cubes[0]:
                    round_cubes[0] = result[0]

            elif result[1] == "green":
                if result[0] > round_cubes[1]:
                    round_cubes[1] = result[0]

            elif result[1] == "blue":
                if result[0] > round_cubes[2]:
                    round_cubes[2] = result[0]

    game_power = round_cubes[0] * round_cubes[1] * round_cubes[2]
    power_sum += game_power

    game_power = 0
    round_cubes = [0, 0, 0]

print(power_sum)
