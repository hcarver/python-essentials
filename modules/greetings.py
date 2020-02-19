PUN_WORDS = [
    'skill',
    'whale',
    'fin',
    'fish',
    'swim',
    'orca',
    'shark',
]


def capitalize_puns(name):
    """Capitalize 'pun' components in name and make the rest lowercase.

    Example usage:
    >>> capitalize_puns('Mark Whaleburg')
    'mark WHALEburg'
    """
    name = name.lower()
    for pun in PUN_WORDS:
        name = name.replace(pun, pun.upper())
    return name


def create_greeting(name):
    """Create a greeting string addressed to the input name

    Puns in the name will be capitalized, and a greeting word prepended.
    """
    display_name = capitalize_puns(name)
    greeting_word = "Hi"
    return greeting_word + " " + display_name


"""
IMPORTING WITH AN ALIAS
-----------------------

At the moment, `greeting_word` is hardcoded as "Hi" in the `create_greeting` function.

Instead, set it equal to the output of the (badly named) `create_greeting()`
function located in the `useful_functions` module. There's a problem here though
 - the function that you need to import has the same name as the
`create_greeting` function in this module.

* Import the `create_greeting` function from `useful_functions` with an alias,
so its name doesn't clash with the `create_greeting` in this module.
* Call this function in place of the hardcoded `"Hi" above.
* Run the script `exercises.py` and ensure the greetings are still being printed
"""


"""
IMPORTING VS RUNNING AS A SCRIPT
--------------------------------

Update this module (`greetings`) so that it can be run as a script, and will
print a single greeting to the example name below. This should only display when
the module is run as a script, and not when it is imported.

* Uncomment the first print statement below to print out the value of __name__
   * Run this module as a script (`python3 greetings.py`) and verify that
     __name__ has the value "__main__".
   * Now run the exercises module as a script (`python3 exercises.py`) and
     verify that __name__ now has the value "greetings" instead of "__main__"
     when the greetings module is imported.

* Uncomment the remaining 3 lines of code, and add code that means they only
  run when `greetings.py` is run as a script. Run both `greetings.py` and
  `exercises.py` as scripts and verify that the greeting to Alec Baldfin is only
  displayed when `greetings.py` is run as a script.
"""

# print("\nThe greetings module has the __name__:", __name__)

# print("Running greetings.py as a script")
# example_name = "Alec Baldfin"
# print(create_greeting(example_name))
