"""An introduction to dicts in Python"""

from pprint import pprint

# This imports some dicts into your script - you can ignore this (but don't delete it)
# ------------------------------------------------------------------------------------------
# Lists of the female and male names given to more than 1000 children in the US in the 1990s
from example_data import (
    girls_names_2010,
    boys_names_2010,
    girls_names_1960,
    boys_popularity_by_decade,
)
# ------------------------------------------------------------------------------------------

"""
INTRODUCTION TO DICTS
---------------------
"""
# girls_names_2010 is a dictionary mapping from lowercase name to the number
# of girls born in 2010 with that name. For example:
# {
#     'sydney': 4328,
#     'camila': 4300,
#     'kaitlyn': 3290,
# }
#
# Uncomment the pprint line below and run the script to see what the
# variable girls_names_2010 looks like. It is quite long, so you'll probably
# want to re-comment the line afterwards to keep your display clearer.
# ~~~~~~~~~~~~~~~~~~~~~~~~
# pprint(girls_names_2010)
# ~~~~~~~~~~~~~~~~~~~~~~~~

# print()
# print("There are ... names in girls_names_2010")
# print("There are ... names in boys_names_2010")

"""
ACCESSING DICT VALUES
---------------------
"""

# print()
# print("In 2010 there were", "...", "boys named Maximus")
# print("In 2010 there were", "...", "girls named Terry")

"""
UPDATING DICT VALUES
--------------------
"""

# <<< YOUR CODE HERE >>>

# print()
# print("In 2010 there were", boys_names_2010['killian'], "boys named Killian")
# print("In 2010 there were", girls_names_2010['whailey'], "girls named Whailey")

"""
REMOVING ITEMS
--------------
"""

# print()
# print("There were", len(girls_names_2010), "names in girls_names_2010")
#
# # You only need to change this line of code
# print("There were", "...", "girls named Leeann")
#
# print("There are now", len(girls_names_2010), "names in girls_names_2010")
# if 'leeann' in girls_names_2010:
#     print('Leeann has not been removed!')

"""
TESTING FOR MISSING KEYS
------------------------
"""

# print()
# print("There were", boys_names_2010['geoff'], "boys named Geoff")
# print("There were", girls_names_2010['henry'], "girls named Henry")

"""
FETCHING VALUES WITH GET
------------------------
"""

name = 'dom'
fallback_name = 'dominic'

# print()
# print("There were", boys_names_2010[name], "boys named", name.title())

"""
ITERATING THROUGH A DICT
------------------------
"""

# Initialize a dictionary containing the count of each letter
names_per_letter = {}

# Write code which iterates through girls_names_2010, and updates
# names_per_letter so that it maps from each letter to the number of
# names starting with that letter.

# <<< YOUR CODE HERE >>>

# print()
# print("There were", names_per_letter.get("j", 0), "girls names starting with J")
# print("There were", names_per_letter.get("q", 0), "girls names starting with Q")

"""
DICT VALUES
-----------
"""

highest_boys_name_count = "..."
second_most_popular_girls_name_count = "..."

# print()
# print("The most popular boys name in 2010 was given to", highest_boys_name_count, "boys")
# print("The second most popular girls name in 2010 was given to", second_most_popular_girls_name_count, "girls")

"""
ITERATING THROUGH DICT ITEMS
----------------------------
"""

# Initialize a dictionary containing the count of each letter
popularity_change = {}

# Write code here which iterates through girls_names_2010.items(), and adds
# each name as a key to change_in_popularity. The corresponding value should be
# the difference between the number of girls given the name in 2010 and the
# number given the name in 1960 (from girls_names_2010).
#
# So if there were 47 girls called hilda in 2010, and 458 in 1960, then the
# popularity_change['hilda'] should equal 411  (47 - 458)

# <<< YOUR CODE HERE >>>

# print()
# print("The popularity of Maureen has changed by", popularity_change.get('maureen', 0))
# print("The popularity of Madison has changed by", popularity_change.get('madison', 0))

"""
NESTED DICTS
------------
"""

# print()
# print("boys_popularity_by_decade has type:", type(boys_popularity_by_decade))
# print("containing", len(boys_popularity_by_decade), "items")
# print("it's keys are:", list(boys_popularity_by_decade.keys()))
# print("In 1970, there were", "...", "boys born named Uriel")

# Add code to print the number of baby boys born called Ethan each decade e.g.
# "In 1960 there were 1000 boys born named Ethan"
# "In 1970 there were 1000 boys born named Ethan"
# etc.

# <<< YOUR CODE HERE >>>
