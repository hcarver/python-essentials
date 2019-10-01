"""An introduction to lists in Python"""

# This imports some lists into your script - you can ignore this (but don't delete it)
# ------------------------------------------------------------------------------------------
# Lists of the female and male names given to more than 1000 children in the US in the 1990s
from example_data import girls_names, boys_names
# ------------------------------------------------------------------------------------------

"""
INTRODUCTION TO LISTS
---------------------
"""

cat_name_shortlist = [
    'Catpurrnicus',
    'Shakespaw',
    'Emily Lickinson',
    'Oedipuss',
]

# print("Your shortlist contains ... names:")
# print(cat_name_shortlist)

"""
INDEXING INTO LISTS
-------------------
"""

# print()
# print("Total number of girls names:", len(girls_names))
# print("The most popular girls name was", "...")
# print("The fourth most popular girls name was", "...")
# print("The second least popular girls name was", "...")

"""
SLICING
-------
"""

# print()
# print("The 3 most popular girls names were:", [])
# print("The 4th to 6th (inclusive) most popular girls names were:", [])
# print("The 3 least popular girls names were:", [])
# print(
#     "The first three letters of the least popular girls name are",
#     "...",
# )

"""
COMBINING AND UPDATING LISTS
----------------------------
"""

updated_shortlist = []

# print()
# print("The updated shortlist contains", len(updated_shortlist), "items:")
# print(updated_shortlist)

"""
ITERATING THROUGH A LIST WITH WHILE / POP
-----------------------------------------
"""

# This line just creates a copy of updated_shortlist,
shortlist_to_print = updated_shortlist[:]

# print()
# print('Updated shortlist in reverse:')
while False:
    print("...")

"""
ADVANCED SLICING
----------------
"""

alternating_names = updated_shortlist

# print()
# print("Alternating names on the shortlist:", alternating_names)

secret_code = "!ZagFenaZiahcnsimHlatSMF JAdwteobrXaeK trgsksaZbMWm AOeWrvhP'HAunyoVGYx kNvxbhfm"
# print("The code says:")
# print(secret_code)

"""
IN AND FOR LOOPS
----------------
"""

unisex_names = []

# Insert for loop here

# print()
# print("There are", len(unisex_names), "unisex names:")
# print(unisex_names)

"""
LISTS OF LISTS
--------------
"""

pet_names = [
    ['cat', ['Catpurrnicus', 'Cat Stevens', 'Emily Lickinson']],
    ['dog', ['Bark Wahlberg', 'Droolius Caesar', 'Dogstoyevsky', 'Jack Spaniels']],
    ['rabbit', ['David Hasselhop', 'Rabbit De Niro']],
    ['elephant', ['Donald Trunk', 'Donald Tusks', 'Cinderelephant']],
]

# print()
# print("The first dog name is", "...")
# print("There are", "...", "suggested rabbit names")
# print("The first two elephant names are", "...")
