"""An introduction to class inheritance in Python"""


class Company:
    def __init__(self, name, employees, contractors):
        self.name = name
        self.employees = employees  # A list of employees
        self.contractors = contractors  # A list of contractors

    def list_people(self):
        """Print details of the people working at the company"""
        print("People working at", self.name + ":")

        for employee in self.employees:
            print('* ', employee.description())

        for contractor in self.contractors:
            print('* ', contractor.description())


class Person:
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title

    def description(self):
        """Return a description string e.g. 'Dave the engineer"""
        return self.name + ", the " + self.job_title


"""
1. CREATE SUBCLASSES OF PERSON
------------------------------

The class `Company` is initialized with a list of the contractors and employees
who work there, and can print their details using the `list_people()` method.

At the moment, all of the contractors and employees in the company have the
class `Person`. You will change this so that contractors have the class
`Contractor` and employees have the class `Employee`.

* Create two new classes `Contractor` and `Employee` which are subclasses of
  `Person`.

* Update the employees 'Geri Hallibut' and 'Free Willy Nelson' so they have the
  newly defined `Employee` class.

* Update the contractors 'Sealion Dion' and 'Goldie Prawn' so they have the
  newly defined `Contractor` class.
"""

# < DEFINE `Contractor` AND `Employee` CLASSES HERE >


employees = [
    Person("Geri Hallibut", "Sea.E.O"),
    Person("Free Willy Nelson", "Digital Sharketing Intern"),
]

contractors = [
    Person("Sealion Dion", "Regional Seals Manager"),
    Person("Goldie Prawn", "Sea Sharp Engineer"),
]

company = Company("Clamazon", employees=employees, contractors=contractors)
company.list_people()


"""
2. OVERRIDE THE `description` METHOD FOR CONTRACTORS
----------------------------------------------------

Currently, the `description` method for any type of Person (Contractor or
Employee) returns a string in the format:
    "Eel Pacino, the Housekelper".

You will change this for the Contractor class you defined above, so instead it
returns a string making clear that the person is a contractor:
    "Eel Pacino, the Housekeeper: CONTRACTOR"

* Override the `description` method on the `Contractor` class above so that it
  returns a string of the form:
      "<name>, the <job_title>: CONTRACTOR"

"""


"""
3. OVERRIDE THE `constructor` FOR EMPLOYEES
-------------------------------------------

Currently, all types of Person (Contractor or Employee) are initialized with
a `name` and `job_title`.

You will change this for the Employee class you defined above, so that it also
has a `years_employed` attribute on each instance.

* Override the `constructor` for the `Employee` class above so that it
  also accepts an argument `years_employed` and sets an attribute of the
  same name on the instance.

* Update the instances of `Employee` you create, so that:
  - Geri Hallibut has been employed for 5 years
  - Free Willy Nelson has been employed for 1 year.

* Override the `description` method on the `Employee` class so that it
  returns a string of the form:
      "<name>, the <job_title> for <years_employed> years"
"""


"""
4. USING `super()` IN SUBCLASSES
--------------------------------

* Update the `__init__` method for `Employee` so it uses `super()` to call
  the constructor for `Person`

* Update the `description` methods for both `Employee` and `Contractor` so they
  call the `description` method on the superclass, and modify the result
  instead of creating the description from scratch.
"""


"""
5. POLYMORPHISM
---------------

* Update the definition of `Company` so that instead of storing a two separate
  lists of `employees` and `contractors`, it just stores one list of `people`.
  This list will contain both employees and contractors.

  (You will need to update the constructor, and the `list_people` method)

* Update the line that starts with `company = Company("Clamazon", ...)` so that
  the updated `Company` class is called correctly.

  (You might want to create a new list, `people`, which contains both employees
  and both contractors)
"""


"""
6. CREATE A CUSTOM STRING CLASS
-------------------------------

* Create a subclass of the `str` class called CustomStr.

* Add a method to CustomStr called `is_palindrome` which returns:
  - `True` if the string is the same when reversed. You can use s[::-1] to
    reverse the string s.
  - `False` otherwise.

* Uncomment all the lines of code at the bottom of this section.
"""

# <<< DEFINE CustomStr HERE >>>


# example_1 = CustomStr(1234321)
# example_2 = CustomStr("do geese see god?")
# example_3 = CustomStr("redivider")
# example_4 = CustomStr(3.3)
#
# print()
# for s in [example_1, example_2, example_3, example_4]:
#     if s.is_palindrome():
#         print(s, "is palindromic!")
#     else:
#         print(s, "is NOT palindromic")
