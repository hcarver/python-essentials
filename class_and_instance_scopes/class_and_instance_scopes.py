class User:
    def __init__(self, name, role, user_id):
        if user_id is None:
            # TODO: Add code here, which sets the value of `user_id` if
            # `user_id` has not been specified.
            pass

        self.validate_role(role)  # Ensure that the role has an allowed value
        self.validate_id(user_id)  # Ensure that the id is a unique integer
        self.user_id = user_id
        self.name = name
        self.role = role
        self.log_user_creation()

    def validate_role(self, role):
        """Raises an exception if role does not have an allowed value"""
        # TODO: Update is_valid_role so it is only true for valid calues
        is_valid_role = True

        # <<< DO NOT CHANGE THIS CODE >>>
        if not is_valid_role:
            self.log(role, "is not a valid role")
            raise ValueError("Invalid role")

    def validate_id(self, user_id):
        """Raises an exception if user_id is not a unique integer"""
        if not isinstance(user_id, int):
            self.log("User id", user_id, "is not an integer")
            raise TypeError("user_id should be an integer")

        # TODO: Update is_unique so that it is only true if the user_id is
        # unique across all Users that have been created
        is_unique = True

        # <<< DO NOT CHANGE THIS CODE >>>
        if not is_unique:
            self.log("User cannot be created with a non unique id:", user_id)
            raise ValueError(f"User id is not unique")

    def log_user_creation(self):
        self.log("User", self.user_id, "-", self.name, "created with role:", self.role)

    def log(self, *args):
        print("USER LOG: ", *args)


"""
1. CLASS ATTRIBUTES
-------------------

The class `User` is initialized with `user_id`, `name` and `role`. The
constructor calls a method `validate_role` to ensure that `role` has an allowed
value, but at the moment this isn't implemented, and all roles are allowed.

* Add the following three class attributes (constants):
    - `ADMIN_ROLE`, which has the value 'admin'
    - `EMPLOYEE_ROLE`, which has the value 'employee'
    - `CUSTOMER_ROLE`, which has the value 'customer'

* Using these class attributes, replace the line `is_valid_role = True` so that
  `is_valid_role` is only true if `role` has one of these three values.

* Refactor the code you've written by adding an additional class attribute
  called `ALLOWED_ROLES` which is a `set` containing the other three allowed
  roles. Make sure that each of the strings 'admin', 'employee', and 'customer'
  only appear once in your class definition.

* Run your code and ensure that you see an error when you try to create a user
  with the 'hacker' role. Once you've done this, comment out the line which does
  this.
"""

user_1 = User("Person 1", "admin", 1)
user_2 = User("Person 2", "employee", 2)
user_3 = User("Person 3", "customer", 3)
user_4 = User("Person 4", "hacker", 4)


"""
2. MUTABLE CLASS ATTRIBUTES
---------------------------

At the moment, `user_id` needs to be specified when creating a new `User`, and
the `id` can take any value. You'll update the class, so that `id`s have to be
unique, and then allow for automatic `id` assignment.

* Add a new class attributes called `all_user_ids` which is initialized as an
  empty `set`.

* Add a line to the constructor so that each time a new `User` is created, its
  `user_id` is added to the set of `all_user_ids`.

* Update the line `is_unique = True` in the `validate_id` method, so that it
  only returns True if the `user_id` hasn't already been used by an existing
  class.

* Uncomment the lines of code below, and run the script - check that you see a
  ValueError saying that user id 123 is not unique.

-------------

* Update the constructor for `User` so that `user_id` is an optional argument,
  with a default value of `None`.

* Add a line to the start of the constructor, so that if `user_id is None`, it
  will be set to the largest `user_id` so far + 1.

* Update the line creating Second Duplicate User below, so that id is no longer
  provided as an argument: `user = User("Second Duplicate User", "employee"`
  Run the script again, and ensure that Second Duplicate User has id 124.

"""

# print()
# user = User("First Duplicate User", "employee", 123)
# user = User("Second Duplicate User", "employee", 123)


"""
3. CLASS METHODS
----------------

* In the `User` class, at least one method would work equally well as a class
  method.

  Identify all the methods for which this is the case, and convert them to
  classmethods.

* Add a new classmethod called `create_customer`, which takes one argument,
  `name`, and returns a new `User` with the 'customer' role, and the given name.

* Uncomment the lines of code below
"""

# print()
# new_customer = User.create_customer("John Belugashi")


"""
4. STATIC METHODS
-----------------

* Uncomment the lines of code below, and run this script. Make sure that you
  understand the output you see.

* Now update the `log` method on the `User` class so it is a static method.

"""

# print()
# User.log("This is a log message sent from outside an instance")
