def remove_extra_spaces(s):
    """Remove additional spaces from a string

    Return a string where multiple spaces are all replaced with single spaces,
    and whitespace is trimmed from the ends of the string.

    Example usage:
    >>> remove_extra_spaces('  Skiller    Whale ')
    'Skiller Whale'

    Note: This could be done more neatly using Python's regular expression
    library `re`. If you want to have a go at rewriting this function with `re`
    then it will be good practice at exploring one of Python's more useful
    packages.
    """
    while '  ' in s:
        s = s.replace('  ', ' ')
    return s.strip()


GREETING_WORDS = [
    'Hi there',
    'Hello',
    'Greetings',
    'Ciao',
]


def create_greeting(*args, **kwargs):
    """Returns a greeting word from the set of `GREETING_WORDS`

    *args and **kwargs are permitted here so the function does not error if it
    is called with arguments. It would be very unusual for this to be useful in
    real code, but in this case it's useful for didactic purposes.
    """
    # TODO: Randomly select one of the GREETING_WORDS instead of "Hi"
    return "Hi"


"""
USING THE STANDARD LIBRARY
--------------------------------

At the moment, the `create_greeting` function in this module returns the word
"Hi", but instead it should return a random member of the set GREETING_WORDS

There is a function `choice` in the `random` package which will return a random 
element of a collection. You can use this to do what is needed.

* Update the function `create_greeting` to address the TODO, and return a random
  member of the `GREETING_WORDS` set.
* Run this module as a script to see a random selection of the greetings. If
  you have updated the function incorrectly then the script will error.
"""


if __name__ == "__main__":
    print("Example greetings:")
    selected_greetings = [create_greeting() for _ in range(10)]
    print(selected_greetings)

    # Ensure that only members of the GREETING_WORDS set are returned
    unexpected_greetings = set(selected_greetings) - set(GREETING_WORDS)
    assert not unexpected_greetings, \
        "Unexpected greetings returned: " + str(unexpected_greetings)
