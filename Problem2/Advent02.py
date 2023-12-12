file_path = "./puzzleInput.txt"  # Replace with the actual file path

integer_string_map = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
                    "six": "6", "seven": "7", "eight": "8", "nine": "9"}


total_sum = 0
with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        insertions = []

        # Collect indices and digits
        for word, digit in integer_string_map.items():
            start = 0
            while True:
                start = line.find(word, start)
                if start == -1:
                    break
                insertions.append((start, digit))
                start += len(word)

        # Sort insertions by index
        insertions.sort(key=lambda x: x[0])

        # Insert digits
        for index, digit in reversed(insertions):
            line = line[:index] + digit + line[index:]

        # Find the first and last digit
        first_digit = next((char for char in line if char.isdigit()), None)
        last_digit = next((char for char in reversed(line) if char.isdigit()), None)

        if first_digit and last_digit:
            total_sum += int(first_digit + last_digit)
print(total_sum)