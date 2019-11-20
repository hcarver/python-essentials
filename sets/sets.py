"""An introduction to sets in Python"""

from timeit import timeit

# Imports some data into your script - you can ignore this (but don't delete it)
# ------------------------------------------------------------------------------

from example_data import words  # A set containing several english words

# A dict with a film genre for each key, and a set of films for each value.
from example_data import films_by_genre

# ------------------------------------------------------------------------------

"""
INTRODUCTION TO SETS
--------------------

This section looks at a set of words, `words`, and tries to find out some basic 
properties of the words.

If you wish to look at the words set, then you can uncomment the print(words) 
line, to get a feel for what the structure looks like.

Replace the Ellipses (...) in the variable definitions below, so the code will 
print out:
* The number of items in the `words` set
* The alphabetically first word in the set
* The alphabetically third last word in the set
* Either "'skiller' is in words" or "'skiller' is not in words",
  depending on whether the word 'skiller' appears in the set of words. 
"""

# print(words)  # This line is just to show you what the words set looks like, feel free to recomment it

number_of_words = ...
first_word = ...
third_last_word = ...

# This variable should be True if "skiller" is in `words` and False otherwise
skiller_is_in_words = ...

# <<< DO NOT CHANGE THE CODE BELOW THIS LINE (except to uncomment) >>>

# print()
# print("There are", number_of_words, "words in the `words` set")
# print("The alphabetically first word is", first_word)
# print("The alphabetically third last word is", third_last_word)
# if skiller_is_in_words:
#     print("'skiller' is in words")
# else:
#     print("'skiller' is not in words")

"""
UNIQUENESS
----------

Replace the pass statement in the for loop below, so that it prints each of the
words in the `words` set that use the same set of letters as the word 'skiller'.

Note: This is different to finding anagrams, since one letter can be used
multiple times. "hoop" and "hop" are not anagrams, but they do use the same set
of letters: {'h', 'o', 'p'} 
"""

# print()
# print("The following words use the same set of letters as 'skiller':")

for word in words:
    pass


"""
EFFICIENT LOOKUP
----------------

Update the function `contains_minus_one` so that it returns True if `collection` 
contains the value -1, and False otherwise. This should work whether the 
collection passed in is a set, a list or a tuple (For this, your code
shouldn't need to test what type of collection you have!).

Uncomment the print statements and run the script. You should now be able to see
how quickly the contains_minus_one function runs for lists and tuples. 

Add code that will test how quickly the contains_minus_one function performs for
a set containing the same items as long_list and long_tuple. Update the print 
statement so the correct number of milliseconds is displayed instead of the
Ellipsis (...).
"""

def contains_minus_one(collection):
    """Returns True if the collection contains -1, and False otherwise

    collection can be a set, list or tuple
    """
    pass


def perform_time_test(collection):
    """Time how long it takes for 5000 membership checks of collection

    This function takes a collection (list, tuple, set, etc)
    """
    time_taken = timeit(lambda: contains_minus_one(collection), number=5000)
    return round(time_taken * 1000, 1)


# Create these in the REPL if you want to take a look at them
long_list = list(range(10000))  # list containing all numbers from 0 to 9999
long_tuple = tuple(long_list)  # tuple containing all numbers from 0 to 9999

# print()
# print("Time for list lookup:", perform_time_test(long_list), "milliseconds")
# print("Time for tuple lookup:", perform_time_test(long_tuple), "milliseconds")
# print("Time for set lookup:", ..., "milliseconds")


"""
ADDING VALUES TO A SET
----------------------

Update the code below so that the print statement will display the number of 
unique two-letter patterns at the start of a word in the `words` set.

To do this, replace `pass` in the `for` loop with code that will add all of the
unqiue two-letter starts of words to the set `two_letter_starts`.

For example, the start of "whale" is "wh", and the start of "who" is also "wh", 
so these two words would only add the string "wh" to `two_letter_starts`.
"""

two_letter_starts = set()

for word in words:
    pass


# <<< DO NOT CHANGE THE CODE BELOW THIS LINE (except to uncomment) >>>

# print()
# print("There are", len(two_letter_starts), "unique two letter word starts")


"""
REMOVING VALUES FROM A SET
--------------------------

Implement the function `remove_items` so that it removes all of the elements in 
`items_to_remove` from the set `s` using the `remove()` method. If 
`items_to_remove` contains additional elements which aren't in `s` then they 
can be ignored.

Implement the function `discard_items` to do the same as `remove_items`, but
use `discard()` instead of `remove()`. This should be a little bit simpler 
than the `remove_items` function.
"""

def remove_items(s, items_to_remove):
    """Remove all of the elements in items_to_remove from the set s

    This should be done using s.remove()
    """
    # <<< YOUR CODE HERE - use the remove method only >>>
    pass


def discard_items(s, items_to_remove):
    """Remove all of the elements in items_to_remove from the set s

    This should be done using s.discard()
    """
    # <<< YOUR CODE HERE - use the discard method only  >>>
    pass


# <<< DO NOT CHANGE THE CODE BELOW THIS LINE (except to uncomment) >>>

test_set_1 = {'a', 'b', 'c', 'd'}
remove_items(test_set_1, {'b', 'd', 'e'})

test_set_2 = {'m', 'n', 'o', 'p'}
discard_items(test_set_2, {'m', 'p', 'q'})

# print()
# assert {'a', 'c'} == test_set_1, f"remove_items failed, test_set_1 is {test_set_1} instead of {{'a', 'c'}}"
# print("remove_items is working as expected")
# assert {'n', 'o'} == test_set_2, f"discard_items failed, test_set_2 is {test_set_2} instead of {{'n', 'o'}}"
# print("discard_items is working as expected")


"""
SET LOGIC
---------

This section uses the dict `films_by_genre`, which has a genre for each key, 
and a set of films for each genre.

{
    'action': {'Guardians of the Galaxy', 'Alien', ...},
    'adventure': {'2001: A Space Odyssey', "Howl's Moving Castle", ...},
    'animation': {'Your Name.', "Howl's Moving Castle", ...},
    ...
}

So, you can get the set of action films with `films_by_genre['action']`

In the code below, replace the three Ellipses (...) with logical set 
operators to find the set of films which have the genres:
* 'crime', but not 'drama'
* 'music', or 'western'
* 'romance', and 'comedy'

Update the variable `unmysterious_sci_fi_thrillers` so that it contains the set 
of films which have both the genres 'science fiction', and 'thriller', but do
not have the genre of 'mystery'  
  
"""

# Uncomment this print statement if you want to have a look at films_by_genre
# print(films_by_genre)

crime_but_not_drama = ...
music_or_western = ...
romance_and_comedy = ...

unmysterious_sci_fi_thrillers = ...

# <<< DO NOT CHANGE THE CODE BELOW THIS LINE (except to uncomment) >>>

# print()
# print("Crime, but not Drama movies:", crime_but_not_drama)
# print("Musical, or Western movies:", music_or_western)
# print("Romcoms (Romantic and Comedy) movies:", romance_and_comedy)
# print("Unmysterious Science Fiction Thrillers:", unmysterious_sci_fi_thrillers)


"""
FROZENSETS - EXTENSION TASK
---------------------------

At the moment, you have films grouped by their genre, but it would also be 
useful to have the data the other way around, so you can see the set of genres 
that each film is tagged with:

genres_by_film = {
    'The Empire Strikes Back': {'adventure', 'action', 'science fiction'}, 
    'Inglourious Basterds': {'thriller', 'drama', 'war', 'action'}, 
    'Scarface': {'thriller', 'drama', 'crime', 'action'}, 
    'Gladiator': {'drama', 'adventure', 'action'}, 
    'Guardians of the Galaxy': {'adventure', 'action', 'science fiction'},
    ...
}

This dictionary tells you what type of film each movie is. Because 
'The Empire Strikes Back' and 'Guardians of the Galaxy' both have the same 
genres ({'adventure', 'action', 'science fiction'}), you could assume that they
are likely to be similar.

1. Create the `genres_by_film` dictionary, using the `films_by_genre` dict. 


Not all possible types of film exist. For example, there aren't any musical 
westerns in this dataset (movies with the genres 'music' and 'western'). 

2. How many different types of film are there in the dataset? (how many 
different sets of genres exist in the `genres_by_film` dictionary). Assign this
value to the variable `number_of_film_types`

(e.g. {"musical"}, {"comedy", "action"}, {"comedy", "adventure"}, 
{"action", "adventure", "drama"} etc. would each be a different 'type' of film)

"""

# <<< WRITE CODE TO UPDATE THESE VARIABLES >>>

genres_by_film = {}
number_of_film_types = ...


# <<< DO NOT CHANGE THE CODE BELOW THIS LINE (except to uncomment) >>>

# print()
# print("Total number of films", len(genres_by_film))
# print("Number of different types of film:", number_of_film_types)
