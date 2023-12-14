file_path = "puzzleInput.txt"

with open(file_path, 'r') as file:
    cards = file.read().splitlines()

total = 0
# A more efficient way would be to use a dictionary to store the winning numbers
for card in cards:
    parts = card.strip().split(" | ")
    winning_numbers = parts[0].split(": ")[1].split(" ")
    card_numbers = parts[1].split(" ")
    
    base = 0
    for number in card_numbers:
        if number != "" and number in winning_numbers:
            base = 1 if base == 0 else base * 2
    total += base

print(total)