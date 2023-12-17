# Solution from: https://github.com/weibell/AoC2023-python/blob/main/day05/part2.py

import re

# Reading the input data
input_data = open('puzzleInput.txt').read().splitlines()

# Creating mappings for each stage
maps = []
for line in input_data[2:]:
    if 'map' in line:
        maps.append(dict())
    elif line != '':
        destination, source, length = [int(value) for value in line.split()]
        maps[-1][range(source, source + length)] = range(destination, destination + length)

# Function for reverse lookup of seed from location
def reverse_lookup_seed(location: int) -> int:
    value = location
    for current_map in reversed(maps):
        value = next(
            (source_range.start + (value - destination_range.start)
             for source_range, destination_range in current_map.items()
             if value in destination_range),
            value  # fallback value if no match is found
        )
    return value

# Processing the initial seed data into ranges
initial_seed_data = [int(seed) for seed in re.findall(r'\d+', input_data[0])]
seed_ranges = [range(start, start + length) for start, length in zip(initial_seed_data[::2], initial_seed_data[1::2])]

# Finding the minimum location that corresponds to a seed range
location = 0
while True:
    potential_seed = reverse_lookup_seed(location)
    if any(potential_seed in seed_range for seed_range in seed_ranges):
        print(location)
        break
    location += 1