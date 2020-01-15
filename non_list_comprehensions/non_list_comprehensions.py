"""An introduction to non-list comprehensions in Python"""

from example_data import word_list


"""
For these section you will use a list of words, `word_list`, and perform some
transformations on this list using list comprehensions

If you wish to look at the words list, then you can uncomment the
`print(word_list)` line to see it in the output.

"""

# print(word_list)


"""
TUPLE COMPREHENSIONS
--------------------

Replace the ellipsis (...) below with a tuple comprehension, which iterates
through code_string, so that `no_vowels` is a tuple containing the characters
of code_string which are not vowels (aeiou), or spaces.

The str.lower() method might come in useful for this: "A".lower() == "a".
"""

code_string = "I aSk yoU all herE - Why hUEl!"

# Tuple containing all characters from mysterious_string except vowels or spaces
no_vowels = ...

# <<< DO NOT CHANGE THE CODE BELOW THIS LINE (except to uncomment print statements) >>>

# print("Encoded message:", code_string)
# print("Decoded characters:", no_vowels)

# The str.join method can be used to convert a list of characters back to a str
# If you'd like to understand how this works, check out the python docs online!
# print("Decoded message", ''.join(no_vowels))


"""
SET COMPREHENSIONS
------------------

Replace the ellipsis (...) below, with a set comprehension, which iterates
through `word_list`, and includes the first three letters for all words
starting with `k`.

For example, if word_list were `['keyhole', 'key', 'door', 'keychain', 'kayak']`
then `k_word_starts` would be `{'key', 'kay'}`
"""

# The set of three letter word starts beginning with k
k_word_starts = ...

# <<< DO NOT CHANGE THE CODE BELOW THIS LINE (except to uncomment) >>>

# print()
# print("There are", len(k_word_starts), "three letter word starts beginning with k:")
# print(k_word_starts)


"""
DICT COMPREHENSIONS
------------------

Replace the ellipsis (...) below, with a dict comprehension, which iterates
through `word_list`, and creates a dict which has a key of a  word, and a value
of the length of that word, only for each word beginning with k in word_list.

For example, if word_list were `['keyhole', 'key', 'door', 'keychain', 'kayak']`
then `k_word_lengths` would be `{'keyhole': 7, 'key': 3, 'keychain': 8, 'kayak': 5}`
"""

# The set of three letter word starts beginning with k
k_word_lengths = ...

# <<< DO NOT CHANGE THE CODE BELOW THIS LINE (except to uncomment) >>>

# print()
# print("The length of each word beginning with k is:")
# print(k_word_lengths)


"""
ADVANCED COMPREHENSIONS
------------------

Replace the ellipsis (...) below, with a dict comprehension, which iterates
through the words in `sentence` and through the letters in each word, and
creates a dict which has a key of one of the letters, and a value of the word
containing that letter, but only if the letter is NOT a vowel (a, e, i, o, u).

For example, if sentence were `['where', 'is', 'my', 'cup']`
then `words_containing_letter` would be
`{'w': 'where', 'h': 'where', 'r': 'where', 's': 'is', 'm': 'my', 'y': 'my',
'c': 'cup', 'p': 'cup'}`
"""
sentence = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

# The dictionary of consonants and the word in sentence which contains them
words_containing_letter = ...

# <<< DO NOT CHANGE THE CODE BELOW THIS LINE (except to uncomment) >>>

# print()
# print("The word in the sentence containing each consonant is:")
# print(words_containing_letter)
