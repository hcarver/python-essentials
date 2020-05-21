"""Exceptions in Python"""

from fortunes import tell_fortune, ask_for_birthday

"""
SYNTAX ERRORS
-------------

The code block below contains several SyntaxErrors. Run this python file (with
python3) and use the SyntaxError messages to identify and fix the errors.

When this code is working, it should print out the numbers 1 to 5, along with
their squares (n * n) on the line below.
"""

for i in range(1, 6) {
     square = i ** 2
    print(str(i), "Squared is:)
	print(square))
     print()
}


"""
HANDLING ERRORS
---------------

The code in this section asks the user to enter their year, month and day of
birth (e.g. 1987, 12 and 25), and then prints out their 'fortune' based on an
old English nursery rhyme (called Monday's child).

* Uncomment the line which calls `tell_birthday_fortune()` and run the script.
  Enter the year, month and day of your birthday (as numbers) in the terminal
  to get your fortune!

* Try entering a string (e.g. "March" instead of the number 3 for the month).
  You should see a `ValueError`, because the string could not be converted to a
  number.

* Add a `try` and `except` block to the `tell_birthday_fortune()` method, so
  that if you enter a non-numeric value for part of the birthday, the code does
  not throw an error, and instead prints a message which says:

  "Invalid Birthday Date!"`

* Update the `except` block, so that if users enter an invalid date, they can
  try again, repeatedly until they have entered valid dates.

  (hint: functions in Python can call themselves)

"""

def tell_birthday_fortune():
    birthday = ask_for_birthday()
    tell_fortune(birthday)


# tell_birthday_fortune()
