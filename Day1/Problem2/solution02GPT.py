# Define a function to calculate the sum of calibration values for the new puzzle
def sum_calibration_values(lines):
    # Mapping of spelled-out numbers to their corresponding digits
    number_map = {
        "one": "1", "two": "2", "three": "3", "four": "4", 
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    total = 0
    for line in lines:
        # Find all occurrences of spelled-out numbers and digits
        found = []
        for word, digit in number_map.items():
            start = 0
            while start < len(line):
                start = line.find(word, start)
                if start == -1:
                    break
                found.append((start, digit))
                start += len(word) # Move past this word
                
            start = 0
            while start < len(line):
                if line[start].isdigit():
                    found.append((start, line[start]))
                start += 1
   

        # Sort the found numbers by their position in the string
        found.sort(key=lambda x: x[0])

        # Extract the digits from the sorted list
        digits = [digit for _, digit in found]
        total += int(digits[0]+digits[-1])
        
    return total 

lines = []

for line in open("./puzzleInput.txt", "r"):
    lines.append(line.strip())

# Calculate the sum of calibration values
ans = sum_calibration_values(lines)
print(ans)