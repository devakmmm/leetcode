import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

# 1) Capitalize suffixes using map()
def capitalize_suffix(name):
    return name.capitalize()

cap_suffixes = list(map(capitalize_suffix, suffixes))

# 2) Generate 10 fantasy names via list comprehension
def create_fantasy_name(list_1, list_2):
    return random.choice(list_1) + ' ' + random.choice(list_2)

random_names = [create_fantasy_name(prefixes, cap_suffixes) for _ in range(10)]

# 3) Pure functions
def fire_in_name(name):
    return 'Fire' in name

def concatenate_names(name1, name2):
    return (f"{name1} + {name2}\n")

# 4) filter() + reduce()
filtered_names = list(filter(fire_in_name, random_names))
reduced_names = reduce(concatenate_names, filtered_names, '')  # initial '' handles empty case

# 5) Display function
def display_name_info(all_names, filtered, reduced):
    print("Generated fantasy names:")
    for n in all_names:
        print(f" - {n}")

    print("\nFiltered names (contain 'Fire'):")
    if filtered:
        for n in filtered:
            print(f" - {n}")
    else:
        print(" (none)")

    print("\nReduced names (concatenated):")
    print(reduced if reduced else "(empty)")

# Run the display
display_name_info(random_names, filtered_names, reduced_names)