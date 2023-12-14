file_path = "puzzleInput.txt"

with open(file_path, "r") as file:
    input = file.readlines()

# Remove the newline character from each line
input = [line.strip() for line in input]

def sum_part_ratios(schematic):
    rows = len(schematic)
    cols = len(schematic[0])
    total = 0

    i = 0
    while i < rows:
        j = 0
        while j < cols:
            if schematic[i][j] == "*":
                numbers = []

                for dx in [-1, 0, 1]:
                    left, right = 0,0
                    for dy in [-1, 0, 1]:
                        nx, ny = i + dx, j + dy
                        if ny <= right:
                            continue
                        if 0 <= nx < rows and 0 <= ny < cols and not (nx == i and ny == j) and schematic[nx][ny].isdigit():
                            left = ny
                            while left >= 0 and schematic[nx][left].isdigit():
                                left -= 1
                            right = ny
                            while right < cols and schematic[nx][right].isdigit():
                                right += 1
                            numbers.append(int(schematic[nx][left+1:right]))

                if len(numbers) == 2:
                    total += numbers[0] * numbers[1]
            j += 1
        i += 1
    return total

print(sum_part_ratios(input))