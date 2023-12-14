file_path = "puzzleInput.txt"

with open(file_path, "r") as file:
    input = file.readlines()

# Remove the newline character from each line
input = [line.strip() for line in input]


def sum_part_numbers(schematic):
    rows = len(schematic)
    cols = len(schematic[0])
    total = 0
    symbols = set("%&=@/*#$+-")
    i = 0
    while i < rows:
        j = 0
        while j < cols:
            if schematic[i][j].isdigit():
                break_outer = False  # Flag variable to break the outer loop
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < rows and 0 <= ny < cols and schematic[nx][ny] in symbols:
                            left = j
                            while left >= 0 and schematic[i][left].isdigit():
                                left -= 1
                            right = j
                            while right < cols and schematic[i][right].isdigit():
                                right += 1
                            number = schematic[i][left+1:right]
                            total += int(number)
                            j = right - 1
                            break_outer = True  # Set the flag to break the outer loop
                            break
                    if break_outer:
                        break
            j += 1
        i += 1
    return total

print(sum_part_numbers(input))