with open("puzzleInput.txt", "r") as file:
    puzzle_input = file.readlines()

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

def is_game_possible(game_data, max_cubes):
    """Check if a game is possible given the maximum number of cubes of each color."""
    for round in game_data:
        if any(round[color] > max_cubes[color] for color in round):
            return False
    return True

# Parse the puzzle input and determine possible games
games_data = [parse_game_data(line) for line in puzzle_input]
max_cubes = {'red': 12, 'green': 13, 'blue': 14}

# Calculate the sum of IDs of possible games
sum_of_possible_game_ids = sum(game_id for game_id, game_data in games_data if is_game_possible(game_data, max_cubes))
print(sum_of_possible_game_ids)