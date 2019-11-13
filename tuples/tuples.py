from pprint import pprint
from timeit import timeit
from sys import getsizeof

from example_data import all_profiles, all_profiles_multishop


"""
INTRODUCTION TO TUPLES
----------------------

Update the function `tuple_from_profile` so that it does what its docstring
says. That is, it should take a dict, `profile`, and return a tuple which 
contains the values for occupation, age, gender, favourite_shop
"""


def tuple_from_profile(profile):
    """
    Takes a profile dict and returns a tuple of profile attributes

    :param profile: A dict mapping from profile attribute names to values.
    :return: A tuple of attributes corresponding to the fields:

    * occupation
    * age
    * gender
    * favourite_shop

    Example usage:

    tuple_from_profile(
         {
            'name': 'Free Willy Nelson',
            'occupation': 'Guitarfish',
            'age': '60+',
            'gender': 'M',
            'favourite_shop': 'Sharks and Spencer',
        },
    )

    Will return:

     ('Guitarfish', '60+', 'M', 'Sharks and Spencer')
    """
    pass


# <<< DO NOT CHANGE THE CODE BELOW THIS LINE (except to uncomment) >>>

example_profile = {
    'name': 'Free Willy Nelson',
    'occupation': 'Guitarfish',
    'age': '60+',
    'gender': 'M',
    'favourite_shop': 'Sharks and Spencer',
}

profile_attributes = tuple_from_profile(example_profile)
# print("Attributes are:", profile_attributes)


"""
SIMILARITIES BETWEEN TUPLES AND LISTS
-------------------------------------

Update the function `dict_from_tuple` so that it does what its docstring
says. That is, it should take a tuple which contains values corresponding to 
occupation, age, gender, and favourite_shop, and return a dictionary containing 
this information. 
"""


def dict_from_tuple(attributes):
    """
    Takes a tuple of attributes, and returns a dict mapping from the
    strings 'occupation', 'age', 'gender', and 'favourite_shop'
    to the corresponding attributes.

    :param attributes: A tuple of attributes:
           (occupation, age, gender, favourite_shop
    :return: A dict mapping from attribute type to attribute values

    Example usage:

        dict_from_tuple(
            ('Brine surgeon', '30-40', 'F', 'Clamazon'),
        )

    Which returns:

        {
            'occupation': 'Brine surgeon',
            'age': '30-40',
            'gender': 'F',
            'favourite_shop': 'Clamazon',
        }
    """

    # <<< ADD YOUR CODE HERE >>>
    pass


# <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>

test_attributes = ('Swimmigration officer', '30-40', 'F', 'John Lewfish')

# print()
# print("Dictionary of attributes:")
# pprint(dict_from_tuple(test_attributes))


"""
DIFFERENCES BETWEEN TUPLES AND LISTS
------------------------------------

The timeit function allows you to test the average length of time for an 
operation. It takes as an argument the string form of a python expression 
(generally not recommended for security reasons...) and measures how long the
evaluation of that expression takes.

The getsizeof function allows you to find the size in memory of an 
object. It takes any object as an argument, and returns the object size in 
bytes. 

You don't need to write any new code, but look at the code below and make sure 
you understand what is being measured.
"""

# Measure the size in-memory of lists and tuples
a_long_list = list(range(100000))  # A list from 0 to 99999
a_long_tuple = tuple(a_long_list)  # A tuple from 0 to 99999

long_list_size = getsizeof(a_long_list)
long_tuple_size = getsizeof(a_long_tuple)

# print()
# print("A long list is", long_list_size/long_tuple_size, "times bigger in memory")


# Measure the amount of time it takes to combine tuples and lists
time_to_add_tuples = timeit('(1, 2, 3) + (4, 5, 6)')
time_to_add_lists = timeit('[1, 2, 3] + [4, 5, 6]')

# print("Adding lists is", time_to_add_lists / time_to_add_tuples, "times slower")


"""
TUPLE UNPACKING
---------------

Refactor `dict_from_tuple` above so that it uses tuple unpacking instead of 
doing any indexing with square brackets.

Update `dict_from_tuple` so that instead of expecting exactly one 
`favourite_shop`, the function can deal with several (or no) favourite shops. 
The tuple it receives will be 3 or more elements long, with the fourth element 
onwards all put into a list for `favourite_shop`.

For example, when called with the tuple
('Carp-enter', '20-30', 'M', 'Clamazon', 'Algi'), 
favourite_shop should be set to ['Clamazon', 'Algi'].
"""


test_attributes_1 = ('Nurse shark', '20-30', 'M', 'sEaBay', 'Algi')
test_attributes_2 = ('Piano tuna', '<5', 'F')

# print("\nTest dictionaries:\n")
# pprint(dict_from_tuple(test_attributes_1))
# print()
# pprint(dict_from_tuple(test_attributes_2))


"""
TUPLES AS KEYS
--------------

The list `all_profiles` contains a large number of customer profiles, which
might hold some useful information for advertising etc. It looks something like:

[
    {'occupation': 'Pilot whale', 'age': '30-40', 'gender', 'F', 'favourite_shop': 'John Lewfish'},
    {'occupation': 'Eelectrician', 'age': '10-20', 'gender', 'F', 'favourite_shop': 'Surfways'},
    ... 
]

You'll need to identify the largest customer segment in terms of occupation, 
age, gender and favourite shop.     

Update the function `get_largest_segment` so it does what its docstring says, 
and returns the dictionary corresponding to the most common profile in 
`profiles`. You can use the `largest_value_and_key` function if you wish.
"""


def largest_value_and_key(d):
    """Return the largest value in dict `d`, and its key"""
    max_value = max(d.values())
    for key, value in d.items():
        if value == max_value:
            return value, key


def get_largest_segment(profiles):
    """Take a list of profiles, and return the most common profile

    :param profiles: A list of profile dictionaries. containing the fields:
           occupation, age, gender and favourite_shop
    :return: A dict representing the most common profile, and its frequency

    Example usage:

    get_largest_segment([
        {'occupation': 'Pilot whale', 'age': '30-40', 'gender': 'F', 'favourite_shop': 'John Lewfish'},
        {'occupation': 'Eelectrician', 'age': '10-20', 'gender': 'F', 'favourite_shop': 'Surfways'},
        {'occupation': 'Pilot whale', 'age': '30-40', 'gender': 'F', 'favourite_shop': 'John Lewfish'},
    ])

    Will return:

    {'occupation': 'Pilot whale', 'age': '30-40', 'gender', 'F', 'favourite_shop': 'John Lewfish'}, 2
    """
    pass


# <<< DO NOT CHANGE THE CODE BELOW THIS LINE (except to uncomment) >>>

# largest_segment, frequency = get_largest_segment(all_profiles)
# print('\nMost common profile occurs', frequency, 'times:')
# pprint(largest_segment)


"""
TUPLES AS KEYS (CONTINUED)
--------------

The list `all_profiles_multishop` contains a large number of customer profiles, 
which each contain more than one favourite_shop, stored in a list.

For example: 

[
    {'occupation': 'Pilot whale', 'age': '30-40', 'gender', 'F', 'favourite_shop': ['John Lewfish', 'Surfways']},
    ... 
]

Trying to use the same function (as done below) will likely fail. Make whatever 
adjustments are required for this function call to succeed, and find the largest 
segment once you account for multiple favourite shops 

(you might also want to change or redefine some other functions in your script)
"""

# largest_multishop_segment, multishop_frequency = get_largest_segment(all_profiles_multishop)
# print('\nMost common multi-shop profile occurs', multishop_frequency, 'times:')
# pprint(largest_multishop_segment)
