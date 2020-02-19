"""An introduction to how modules and the search path work in Python"""

from example_data import SKILLEBRITY_NAMES


print("Running code in the module exercises.py...")


"""
SHARING CODE BETWEEN MODULES
----------------------------

In this section you will be printing out greetings to various 'Skillebrities' 
using the greeting function defined in a different python module (greetings.py).

The code below uses the list `SKILLEBRITY_NAMES`

* Uncomment the two print statements below.
* The code in this section should print out a greeting to each name in the list
  `SKILLEBRITY_NAMES`. A function to generate a greeting from a name already 
  exists in the `greetings` module.
* Replace the ellipsis (...) with a call to the `create_greeting` function in
  the `greetings` module (you will need to add an import statement to this file)
* Run this module (`python3 exercises.py`), and check that you now see printed
  greetings to a few names.
"""

# print("\nGreetings!")

for name in SKILLEBRITY_NAMES:
    greeting = ...
    # print(greeting)


"""
DIFFERENT WAYS TO IMPORT
------------------------

* Update your import from the previous section so that you only import
  the `create_greeting` function from the `greetings` module (instead of
  importing the whole module). Run the script and make sure the output hasn't
  changed.

The greetings that are printed out from the previous section should look a
little bit messy - a lot of the names have badly formatted spaces. To fix this
you'll need to add a line into the `for` loop above which will clean up the
spaces in each greeting. The `useful_functions` module contains a function
`remove_extra_spaces` which will do this for you.

* Import the `remove_extra_spaces` function from the `useful_functions` module.
  Use it in the `for` loop to clean each greeting before printing them.
  Run your script and ensure that the spaces now look sensible.

* Now change your import statement so that it imports everything from the
  `useful_functions` module (using `from useful_functions import *`).
  Make sure that this import is on the line BELOW where you import
  `create_greeting`

* Run the script. You should see that the names have now disappeared from the
  greetings - can you work out why? (you'll need to look at the other files).
    - HINT: What happens if you move the `*` import so it's above the other
      imports

  Change the import back so you are only importing the `remove_extra_spaces`
  function.
"""
