"""An introduction to various looping techniques in Python"""

from example_data import words, word_frequencies
from utils import print_rainbow

# `words` is a tuple containing the ~10000 most common english words used
#  on the english web. They are not in frequency order.
# `word_frequencies` is a tuple of the same length containing their frequencies.
#
# words looks like: ('lib', 'sweet', 'contents', 'photographers', 'vhs', ...)
# word_frequencies looks like: (24291030, 32311923, 78365831, 8306260, 32362671, ...)
# These print lines are just to display the variables, you can leave them commented.

# print(words[:10])
# print(word_frequencies[:10])

"""
ENUMERATE
---------

The code below iterates through all the words in the word list, finds anagrams
of "loop" and prints them out, along with their position in the list.

Refactor this code, so that instead of looping through the indices and looking
up the words, it uses enumerate to make the code tidier
"""

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)


search_word = 'loop'
print("Anagrams of", search_word, "...")

for index in range(len(words)):
    word = words[index]
    if is_anagram(word, search_word):
        print(word, "is in `words` at position", index)


"""
Using enumerate, add code below to create a unique id for each word in `words`.
The first item in `words` should have an id of 1, the second, 2 and so on.
Store these ids in `words_id_dict` so it is a dict with words as keys, and
their ids as values.

Uncomment the print statements below, and make sure that your script runs.

NOTE: As well as doing this in a for loop, you could use a dict comprehension.
"""

word_id_dict = {}

# print()
# print("id for killer:", word_id_dict["killer"])
# print("id for whale:", word_id_dict["whale"])


"""
SORTING AND REVERSE SORTING
---------------------------

The function `print_rainbow` accepts any iterator (anything that can be
looped through in a for loop), and prints out the first 7 words.

Uncomment the lines of code below. At the moment, `sorted_words` is equal to
the `words` tuple.

Update this so that `sorted_words` contains the words sorted alphabetically,
and update the final `print_randow` statement, so that it will print the
words sorted in reverse (alphabetically last is printed first)
"""

sorted_words = words

# print()
# print("The first words are:")
# print_rainbow(sorted_words)
# print("The last words are:")
# print_rainbow([])


"""
SORTING WITH KEYS
-----------------

Uncomment the code at the bottom of this section.

Replace the empty lists in the definitions below so that each of the lists is
a sorted version of `words` as follows:

* `longest_words` should be sorted by length, with the longest word appearing
  at the start of the list.

* `custom_sorted` should be sorted in reverse alphabetical order, but with
  the first letter removed. For example, ['azure', 'turquoise', 'blue', 'teal']
  is sorted in this way (using 'zure', 'urquoise', 'lue', 'eal')
"""

longest_words = []

# This should be the words sorted in reverse alphabetical order, when excluding
# the first letter:
custom_sorted = []

# print()
# print("The longest words are:")
# print_rainbow(longest_words)
# print("The alphabetically last words excluding the first letter are:")
# print_rainbow(custom_sorted)


"""
SORTING ON MULTIPLE CRITERIA
----------------------------

Uncomment the code at the bottom of this section.

Replace the empty lists in the definitions for `longest_words_alphabetical`
so that it contains the `words` sorted by length, but with ties decided
alphabetically, so that the alphabetically first word comes first when two
words have the same length.

For example: ["krill", "shark", "shoal" "whale", "fish", "cod"]
"""

# This should be the words sorted by length, but with ties decided
# alphabetically when two words are the same length.
longest_words_alphabetical = []

# print()
# print("The longest words (with ties decided alphabetically) are:")
# print_rainbow(longest_words_alphabetical)


"""
COMBINING ITERABLES WITH ZIP
----------------------------

Uncomment the two print statements in the code in this section.

This code searches for anagrams of the word 'post', and prints them, along with
their frequency on the web. At the moment it does this by iterating through the
index of the words.

Update the code, so it instead uses `zip` to iterate through `words` and
`word_frequencies` at the same time.
"""

search_word = "post"
# print()

for index in range(len(words)):
    word = words[index]
    if is_anagram(word, search_word):
        frequency = word_frequencies[index]
        # print(word, "is in `words` and occurs", frequency, "times")


"""
COMBINING ZIP AND SORTED
------------------------

Uncomment the `print` and `print_rainbow` statements at the bottom of this section.

Update `sorted_words_and_frequencies` so that it is a list containing tuples of
(word, word_frequency), sorted so that the words with the highest frequencies
come at the top:

[('most popular word', 12345), ('next most popular word', 12241), ... ]

Do this using `zip` and `sorted` with a `key`.
"""

sorted_words_and_frequencies = []

# print()
# print("Most common words on the english web and their frequencies:")
# print_rainbow(sorted_words_and_frequencies)


"""
UNZIPPING
---------

Uncomment the `print` and `print_rainbow` statements at the bottom of this section.

Using `sorted_words_and_frequencies` defined above, update `most_popular_words`
so that it is just a list of words, and doesn't include their frequencies.
"""

most_popular_words = []

# print()
# print("Most common words on the english web:")
# print_rainbow(most_popular_words)


"""
REVERSED
---------

Uncomment the `print` and `print_rainbow` statements at the bottom of this section.

Using `reversed`, update the call to `print_rainbow`, so that it receives
the reverse of `most_popular_words`. This should then print out the
words which have the lowest frequencies in the common words list.
"""

# print()
# print('Least common "common words" on the english web:')
# print_rainbow([])
