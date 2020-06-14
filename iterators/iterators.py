"""Python Iterators"""

import time

# The constants and function here are helpers for the exercises. You don't need
# to change any of the code here (if you do, then the exercises might break!)

VOWELS = set('AEIOU')
CONSONANTS = set('BCDFGHJKLMNPQRSTVWXYZ')

def vowel_requested():
    # Returns True if the user requests a vowel, and False otherwise (consonant)
    while True:
        response = input('\nWould you like a vowel (v) or a consonant (c)? ')
        if response.lower() == 'v':
            return True
        elif response.lower() == 'c':
            return False
        else:
            print("Please enter the letter 'c' or 'v' and then press Enter")


"""
USING ITERATORS
---------------

In the British game show, Countdown, there is a round where contestants have to
make the longest word they can with 9 letters.

At the start, a contestant picks random letters one at a time, and can choose
whether to pick a consonant or vowel. Once a letter has been picked, it can
not be picked for a second time.

The function `select_countdown_letters` implements this by popping items from
a `set` of vowels, and a `set` of consonants. For each letter it uses the
function `vowel_requested` to ask the user if they would like a vowel (True)
or consonant (False).

At the moment this function modifies the original sets `VOWELS` and
`CONSONANTS`, (because `set.pop()` modifies the set).

* Use iterators to update this function so that it no longer modifies the sets.
  It should still only return each vowel and consonant at most once (no repeated
  letters).

  To do this you should:
    - Create new iterators for the sets `VOWELS` and `CONSONANTS`.
    - Use these iterators to return values instead of popping them from a set.
"""


def select_countdown_letters():
    letters = ''

    for _ in range(9):
        if vowel_requested():
            next_letter = VOWELS.pop()
        else:
            next_letter = CONSONANTS.pop()

        letters += next_letter
        print('Your letters are:', letters)

    return letters


print('\n', 'Your set of letters is:', select_countdown_letters(), '\n')

#  Make sure that the original letter sets have not been changed
assert VOWELS == set('AEIOU'), 'the constant VOWELS has been modified'
assert CONSONANTS == set('BCDFGHJKLMNPQRSTVWXYZ'), 'the constant CONSONANTS has been modified'


"""
CUSTOM ITERATORS
----------------

The code below contains a simple `ShoppingBasket` class, which keeps track of a
list of `Item`s.

* Uncomment the lines of code at the bottom of this section.

* Run the code. You should see this error:
      TypeError: 'ShoppingBasket' object is not iterable
  This is because the code attempts to iterate through a `ShoppingBasket`
  instance, and the class does not have the required method.

* Update the `ShoppingBasket` class so that it is an iterable. Iterating through
  the shopping basket should behave the same as iterating through its list of
  Items.

--------------------------------------------------------------------------------

* Extension: If you finish the previous exercises then update the for loop,
  so that instead of printing item.name, it prints item_name:

  for item_name in my_basket:
      print(item_name)

* Now update ShoppingBasket so that it iterates through item names,
  instead of the item objects. You will need to create a custom iterator class.
"""


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingBasket:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)


my_basket = ShoppingBasket()
my_basket.add_item(Item("Butter", 1.00))
my_basket.add_item(Item("Toothpaste", 1.50))
my_basket.add_item(Item("Lightbulb", 4.00))
my_basket.add_item(Item("Tofu", 3.20))


# print("\nShopping basket contains:")
# for item in my_basket:
#     print(item.name)


"""
A CUSTOM RANGE CLASS
--------------------

The built-in `range` function that you may have come across in Python isn't
actually a function; it's an iterable class that lets you iterate over integers.
For example: `for i in range(3, 7)` would iterate over the values 3, 4, 5, 6,
assigning each value to the variable i. Notice that the sequence doesn't return
the end value (7).

The `CustomRange` class below will replicate the behaviour of `range`, taking
in `start` and `end` values for a sequence of numbers.

It will also accept a `transform` argument. This should be a function that
takes in a value, and returns the next value in a sequence. If you wanted a
sequence that increased by 5 each time, `transform` would be: `lambda x: x + 5`

For example

CustomRange(10, 30, transform=lambda x: x + 5) should generate the sequence 10, 15, 20, 25
CustomRange(2, 20, transform=lambda x: 2*x - 1) should generate the sequence 2, 3, 5, 9, 17


* Uncomment the lines of code at the bottom of this section

* Update the methods `__iter__` and `__next__` on `CustomRange` so that the
  iterations at the bottom of this file work correctly

* You will have to add a new attribute to CustomRange to keep track of the
  current iteration position, and update this in the `__iter__` and `__next__`
  methods.

* Run the code and make sure that the sequences printed look correct.
"""


class CustomRange:
    def __init__(self, start, end, transform=lambda x: x + 1):
        self.start = start
        self.end = end
        self.transform = transform

    def __iter__(self):
        pass

    def __next__(self):
        pass


# # This should print odd numbers between 40 and 50: 41, 43, 45 etc.
# print('\nOdd numbers from 40 to 50')
# for i in CustomRange(41, 50, lambda x: x + 2):
#     print(i)

# # This should print all the powers of 2 less than 100: 1, 2, 4, 8, etc.
# print('\nPowers of 2 up to 100')
# for i in CustomRange(1, 100, lambda x: x * 2):
#     print(i)

# # Each iteration should return the square of the previous number:
# # 2, 4, 16, 256 etc. up to 10 billion.
# print('\nRepeated squares up to 10 billion')
# for i in CustomRange(2, 10000000000, lambda x: x ** 2):
#     print(i)


"""
INFINITE ITERABLES
------------------

* Uncomment the lines of code at the bottom of this section. If you try to run
  this program at the moment, it will break because InfiniteCycle is not an
  iterable.

* Without changing the code in the for loop, update the InfiniteCycle class so
  that it is an iterable which cycles through all of its items without ever
  terminating. For example:

  for item in InfiniteCycle([1, 2, 3]):
      print(item)

  should print out the numbers 1, 2, 3, 1, 2, 3, 1, 2, 3, ... etc.
"""

class InfiniteCycle:
    def __init__(self, items):
        self.items = items


# print("This will go on for")
# for item in InfiniteCycle(["ever", "and"]):
#     time.sleep(1)  # Wait 1 second
#     print(item)
