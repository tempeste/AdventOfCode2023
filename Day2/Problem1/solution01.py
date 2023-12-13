file_path = "puzzleInput.txt"  # Replace with the actual file path

with open(file_path, "r") as file:
    games = file.readlines()

# The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
total = 0
for game in games:
    # Strip to remove the newline character
    parts = game.strip().split(": ")
    game_number = int(parts[0].split(" ")[1])
    rounds = parts[1].split("; ")
    
    cube_map = {"red": 0, "green": 0, "blue": 0}
    for round in rounds:
        cubes = round.split(", ")
        for cube in cubes:
            number , color = cube.split(" ")
            if cube_map[color] < int(number):
                cube_map[color] = int(number)
    
    if cube_map["red"] <= 12 and cube_map["green"] <= 13 and cube_map["blue"] <= 14:
        total += game_number

print(total)
        
            
            