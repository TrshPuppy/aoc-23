# which games would have been possible if the bag contained
# only 12 red cubes, 13 green cubes, and 14 blue cubes
total_red = 12
total_green = 13
total_blue = 14
total_cubes = total_blue + total_green + total_red
possible_games = 0


# Major game loop:
for i, line in enumerate(input.split(f"\n")):
    # Chop off 'Game X:' portion of string
    chopped_line = line.split(f":")[1]
    game_cubes = [0, 0, 0]

    # Loop through game to get rounds:
    for round in chopped_line.split(f";"):
        round_cubes = [0, 0, 0]  # r, g, b
        round_total = 0
        impossible = False

        # Loop through round to get colors:
        for cubes in round.split(f","):
            print("TOSS: " + cubes)

            # Break toss into number and color [number, color]
            result = [int(cubes.split(" ")[1]), cubes.split(" ")[2]]
            round_total += result[0]

            # Get results for cube colors thrown and add to round results:
            if result[1] == "red":
                round_cubes[0] += result[0]
                game_cubes[0] += result[0]
            elif result[1] == "green":
                round_cubes[1] += result[0]
                game_cubes[1] += result[0]
            elif result[1] == "blue":
                round_cubes[2] += result[0]
                game_cubes[2] += result[0]

        if round_total > total_cubes:
            impossible = True
            break

        if round_cubes[0] > total_red:
            impossible = True
            break

        if round_cubes[1] > total_green:
            impossible = True
            break

        if round_cubes[2] > total_blue:
            impossible = True
            break

    if not impossible:
        possible_games += i + 1

print("POSSIBLE GAMES: " + str(possible_games))
