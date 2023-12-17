file_path = "puzzleInput.txt"

with open(file_path) as f:
    puzzle_input = f.read().splitlines()


seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []
mapOfListsToUpdate = {"seed-to-soil map:" : seed_to_soil, "soil-to-fertilizer map:" : soil_to_fertilizer, "fertilizer-to-water map:" : fertilizer_to_water, "water-to-light map:" : water_to_light, "light-to-temperature map:" : light_to_temperature, "temperature-to-humidity map:" : temperature_to_humidity, "humidity-to-location map:" : humidity_to_location}

list_to_update = []
for idx, line in enumerate(puzzle_input):
    if idx == 0:
        seeds = puzzle_input[idx].strip().split("seeds: ")[1].split(" ")
        seeds = [int(x) for x in seeds]
        continue
    
    if line == "":
        continue
    
    if line in mapOfListsToUpdate:
        list_to_update = mapOfListsToUpdate[line]
        continue
    else:
        line = line.strip().split(" ")
        line = [int(x) for x in line]
        list_to_update.append(line)

def map_value(value, mapping):
    """
    Maps a given value using a provided mapping. If the value is not explicitly
    mapped, it returns the same value.
    """
    for dest_start, src_start, length in mapping:
        if src_start <= value < src_start + length:
            return dest_start + (value - src_start)
    return value


def process_almanac(seeds, *maps):
    """
    Processes the almanac, converting seed numbers through various categories
    until reaching the location number. Returns the lowest location number.
    """
    min_location = float('inf')
    
    for seed in seeds:
        current_value = seed
        for mapping in maps:
            current_value = map_value(current_value, mapping)
        min_location = min(min_location, current_value)

    return min_location

# Process the almanac
lowest_location = process_almanac(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, 
                                  water_to_light, light_to_temperature, temperature_to_humidity, 
                                  humidity_to_location)

print(lowest_location)