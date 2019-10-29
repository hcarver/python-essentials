"""An introduction to functions in Python"""

from pprint import pprint

# This imports some data into your script - you can ignore this (but don't delete it)
# ------------------------------------------------------------------------------------------
# Lists of the female and male names given to more than 1000 children in the US in the 1990s
from example_data import (
    boys_popularity_by_decade,
    girls_popularity_by_decade,
)

girls_names_2010 = girls_popularity_by_decade[2010]
boys_names_2010 = boys_popularity_by_decade[2010]

# pprint(girls_names_2010)
# pprint(boys_names_2010)
# pprint(boys_popularity_by_decade)
# pprint(girls_popularity_by_decade)

# ------------------------------------------------------------------------------------------

"""
PARAMETERS AND ARGUMENTS
------------------------
"""

# <<< YOUR FUNCTION HERE >>>

# print_number_of_names('catherine', girls_popularity_by_decade, 2010)
# print_number_of_names('kathryn', girls_popularity_by_decade, 2010)
# print_number_of_names('katharine', girls_popularity_by_decade, 2010)
# print_number_of_names('katherine', girls_popularity_by_decade, 2010)
# print_number_of_names('catharine', girls_popularity_by_decade, 2010)

"""
POSITIONAL AND KEYWORD ARGUMENTS
--------------------------------
"""

# print()
# print_number_of_names('hailey', 2010, girls_popularity_by_decade)
# print_number_of_names(2010, 'hayley', girls_popularity_by_decade)
# print_number_of_names(girls_popularity_by_decade, 'haylee', 2010)
# print_number_of_names('haley', girls_popularity_by_decade, 2010)

"""
RETURNING VALUES
----------------
"""

# <<< YOUR CODE HERE >>>

# print()
# print("The most popular girls name in 2010 was:", most_popular_name(girls_popularity_by_decade[2010]))
# print("The least popular girls name in 2010 was:", least_popular_name(girls_popularity_by_decade[2010]))

# most_popular, least_popular = get_extreme_names(boys_popularity_by_decade[2010])
# print("The most popular boys name in 2010 was:", most_popular)
# print("The least popular boys name in 2010 was:", least_popular)

"""
MULTIPLE RETURN STATEMENTS
--------------------------
"""

def contains_word(name, word):
    pass


# Edit this function so it returns True if name contains all the letters of
# orca, and false otherwise
def contains_orca(name):
    pass


# print()
# for name in boys_popularity_by_decade[1970]:
#     if contains_orca(name):
#         print(name, "contains the letters from orca")


# print()
# test_word = 'krill'
# for name in boys_popularity_by_decade[1970]:
#     if contains_word(name, test_word):
#         print(name, "contains the letters from", test_word)


"""
VARIABLE LENGTH ARGUMENT LISTS
------------------------------
"""

def longest_name(name_1, name_2):
    if len(name_1) > len(name_2):
        return name_1
    else:
        return name_2

# print()
# print("Longest name of two:", longest_name('dominique', 'quinton'))
# print("Longest name of four:",
#       longest_name('dominique', 'quinton', 'humberto', 'guillermo'))
# print("Longest name of none:", longest_name())


"""
VARIABLE LENGTH KEYWORD ARGUMENT LISTS
--------------------------------------
"""

def most_popular_name(joaquin, monique):
    """each argument is the popularity of the name"""
    if joaquin >= monique:
        return 'joaquin'
    else:
        return 'monique'

# print()
# print("Most popular name of two:", most_popular_name(joaquin=23, monique=42))
# print("Most popular name of four:",
#       most_popular_name(dominique=32, quinton=45, humberto=91, guillermo=3))
# print("Most popular name of none:", most_popular_name())

