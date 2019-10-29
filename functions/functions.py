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


"""
MULTIPLE ARGUMENT TYPES IN ONE FUNCTION
---------------------------------------
"""

# Do not edit this function
def print_details(name, *friends, age=1, **favourites):
    print("My name is", name)
    years_string = "year" if age == 1 else "years"
    print("I am", age, years_string, "old")
    print("I am friends with:")
    for friend in friends:
        print("*", friend)

    for key, value in favourites.items():
        print("My favourite", key, "is", value)

# The call to print_details below should print:
"""
My name is Skiller Whale
I am 1 year old
I am friends with:
* Fin Diesel
* Whaleiam Shakespeare
My favourite island is Majorca
My favourite music is orcastral
My favourite flower is the orcaid
"""

print()
print_details(...)


"""
FUNCTIONS AS OBJECTS
--------------------
"""

boys_names = list(boys_popularity_by_decade[2010])


def longer_than_ten(name):
    """Returns True if name is more than 10 letters long, False otherwise"""
    return []

# assert longer_than_ten("Averylongname") is True, "Averylongname is longer than 10"
# assert longer_than_ten("Tenletters") is False, "Tenletters is not longer than 10"

def starts_with_x(name):
    """Returns True if name starts with x, and False otherwise"""
    return []

# assert starts_with_x("xenia") is True, "xenia starts with x"
# assert starts_with_x("alexander") is False, "alexander does not start with x"

def filter_names(filter_fun, names):
    """Filter a list of names, returning those where filter_fun(name) is True"""
    return names


# Don't edit any of the code below here (except to uncomment)

# print()
# print("Names longer than ten letters:")
# for name in filter_names(longer_than_ten, boys_names):
#     print("*", name)
#
# print()
# print("Names which start with x:")
# for name in filter_names(starts_with_x, boys_names):
#     print("*", name)


"""
LAMBDA FUNCTIONS
----------------
"""

# print()
# print("Names that are two letters long:")
# for name in filter_names(..., boys_names):
#     print("*", name)
#
# print()
# print("Names which start with y:")
# for name in filter_names(..., boys_names):
#     print("*", name)
