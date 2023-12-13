with open("puzzleInput.txt", "r") as file:
    puzzle_input = file.readlines()

def find_minimum_cubes(game_data):
    """Find the minimum number of cubes of each color needed for a game."""
    min_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for round in game_data:
        for color in round:
            min_cubes[color] = max(min_cubes[color], round[color])
    return min_cubes

def calculate_power(cube_set):
    """Calculate the power of a set of cubes."""
    return cube_set['red'] * cube_set['green'] * cube_set['blue']

def parse_game_data(game_line):
    """Parse a line of game data into a structured format."""
    parts = game_line.strip().split(': ')
    game_id = int(parts[0].split(' ')[1])
    rounds = parts[1].split('; ')

    cubes = []
    for round in rounds:
        cube_counts = {'red': 0, 'green': 0, 'blue': 0}
        colors = round.split(', ')
        for color in colors:
            count, color_name = color.split(' ')
            cube_counts[color_name] = int(count)
        cubes.append(cube_counts)
    return game_id, cubes

# Find the minimum cubes for each game and calculate their power
games_data = [parse_game_data(line) for line in puzzle_input]
min_cubes_per_game = [find_minimum_cubes(game_data) for _, game_data in games_data]
powers = [calculate_power(cube_set) for cube_set in min_cubes_per_game]

# Sum of the power of these sets
sum_of_powers = sum(powers)
print(sum_of_powers)