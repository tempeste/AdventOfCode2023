# ChatGPT's solution to Advent of Code Problem 1

file_path = "./puzzleInput.txt"  # Replace with the actual file path

total_sum = 0
with open(file_path, "r") as file:
    for line in file:
        # Initialize first and last digit variables
        first_digit = None
        last_digit = None

        for char in line:
            if char.isdigit():
                # Update first digit if not already found
                if first_digit is None:
                    first_digit = char

                # Always update last digit
                last_digit = char

        # Add the combined digits to the sum if both are found
        if first_digit is not None and last_digit is not None:
            total_sum += int(first_digit + last_digit)

print(total_sum)
