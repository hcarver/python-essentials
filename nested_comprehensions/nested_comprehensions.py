"""An introduction to nested list comprehensions in Python"""


"""
UNROLLING NESTED LISTS
----------------------

In this section we'll flatten nested lists (sometimes called matrices) to one-dimensional lists.

countries_by_continent contains three lists, one with some countries in Europe, one with some countries in North America, one with some countries in Africa.

Transform it into a one-dimensional list containing all of the countries that appear in countries_by_continent.

1. Uncomment the assert and print statements at the bottom of this section
2. Replace each of the ellipses (...) with a list comprehension so that these 
   variables end up as one-dimensional list.
3. Run the script. If your list comprehensions are correctly defined then you
   should be able to run it without seeing any errors.
"""

countries_by_continent=[
        ['Italy', 'Spain', 'Greece'],
        ['US', 'Canada'],
        ['Kenya', 'Tanzania', 'Morocco', 'Tunisia']
        ]

# please return a flat country list, like ['Italy', 'Spain', ... ,'Tunisia']
countries = ...


# <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>

# print("countries")
# print(countries)

# assert len(countries) == 9, "we expected the list to have 9 elements -- did you flatten it correctly?"
# assert type(countries[0]) == str, "the list has the wrong structure, it should only contain String elements"
# assert countries[0] == 'Italy', "the list doesn't start with the element we expected"



"""
If we use a different type of iterable, such as the dictionary in the following example, we can still use nested comprehensions.

Try to achieve the same outcome as before, but this time you'll be flattening the dictionary named_countries_by_continent.

As you can see, it groups the countries together as in the above example, but also names the groups.

"""

named_countries_by_continent={
        'Europe': ['Italy', 'Spain', 'Greece'],
        'North America': ['USA', 'Canada'],
        'Africa': ['Kenya', 'Tanzania', 'Morocco', 'Tunisia']
        }

# <<< CHANGE THE LINES BELOW HERE  - replace ... with list comprehensions >>>

# please return a flat country list, like ['Italy', 'Spain', ... ,'Tunisia']
named_countries = ...

# <<< DO NOT CHANGE THE LINES BELOW HERE (except to uncomment) >>>

# print("")
# print("named_countries")
# print(named_countries)

# assert len(named_countries) == 9, "we expected the list to have 9 elements -- did you flatten it correctly?"
# assert type(named_countries[0]) == str, "the list has the wrong structure, it should only contain String elements"
# assert named_countries[0] == 'Italy', "the list doesn't start with the element we expected"


"""
CREATING NESTED LISTS
---------------------

There are two lists, called colours and fruit.

First, you will join them together so that each fruit is paired with each colour, like so:
['red', 'Apples'], ['red', 'Peaches'] etc, resulting in 16 colour/fruit pairs.

Second, you will create pairs of number and fruit, so that each fruit and number only appears once, e.g.:
[1, 'Apples'], [2, 'Peaches'] etc, resulting in four pairs.

1. Uncomment the assert and print statements at the bottom of this section
2. Replace each of the ellipses (...) with a list comprehension so that these 
   variables end up as nested list.
3. Run the script. If your list comprehensions are correctly defined then you
   should be able to run it without seeing any errors.

"""

nums = [0, 1, 2, 3]
colours=['red', 'green', 'blue', 'plaid']
fruit = ["Apples", "Peaches", "Pears", "Bananas"]


# please create a structure like [['red', 'Apples'], ['red', 'Peaches'], ... , ['plaid', 'Bananas']]
assorted_fruit = ...

# please create a structure like  [[0, 'Apples'], [1, 'Peaches'], [2, 'Pears'], [3, 'Bananas']]
numbered_fruit = ...

# print("")
# print("assorted_fruit")
# print(assorted_fruit)

# assert len(assorted_fruit) == 16
# assert len(assorted_fruit[0]) == 2
# assert type(assorted_fruit) == list
# assert type(assorted_fruit[0]) == list
# assert assorted_fruit[0][0] == 'red'
# assert assorted_fruit[0][1] == 'Apples'

# print("")
# print("numbered_fruit")
# print(numbered_fruit)

# assert len(numbered_fruit) == 4
# assert len(numbered_fruit[0]) == 2
# assert type(numbered_fruit) == list
# assert type(numbered_fruit[0]) == list
# assert numbered_fruit[0][0] == 0
# assert numbered_fruit[0][1] == 'Apples'
