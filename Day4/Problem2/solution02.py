file_path = "puzzleInput.txt"

with open(file_path, 'r') as file:
    cards = file.read().splitlines()

total = 0
copies = [1 for _ in cards]
# A more efficient way would be to use a dictionary to store the winning numbers
for i, card in enumerate(cards):
    parts = card.strip().split(" | ")
    winning_numbers = parts[0].split(": ")[1].split(" ")
    card_numbers = parts[1].split(" ")

    won = 0
    copy = copies[i]
    for number in card_numbers:
        if number != "" and number in winning_numbers:
            won += 1
    for j in range(i+1, i+won+1):
        copies[j] += 1 * copy

    total += copy

print(total)