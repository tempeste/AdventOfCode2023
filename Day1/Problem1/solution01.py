
file_path = "./puzzleInput.txt"  # Replace with the actual file path

sum = 0
with open(file_path, "r") as file:
    for line in file:
        first, last = "", ""
        for i in range(len(line)):
            if line[i].isdigit():
                first = line[i]
                break
                
        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                last = line[i]
                break
            
        sum = sum + int(f"{first}{last}")

print(sum)
