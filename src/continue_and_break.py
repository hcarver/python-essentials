"""
CONTINUE
--------

Prints the 7 times table, up to 7 times 20. But it skips 7*5, 7*10, 7*15 and 7*20.
"""
for x in range(21):
    if x % 5 != 0:
        print(7, "times", x, "is", x * 7)


"""
BREAK
-----
"""
python_code = "multiple_of_5 = x % 5 == 0  # x % 5 is the remainder when dividing by 5. If it's 0, the number divides exactly by 5."
python_code_tokens = python_code.split()
#for token in python_code_tokens:
#    print(token)


"""
NESTED CONTINUE AND BREAK
-------------------------
"""
python_code = [
    "for x in range(5):  # x will start at 0 and finish at 4".split(),
    "print(5 * x)  # This will print from 0 to 20, going up in 5s".split(),
    "print('x is', x)  # Print x as well".split()
    ]
#for line in python_code:
#    for token in line:
#        print(token)
