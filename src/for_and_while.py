def rot13(char):
    keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vals = "NOPQRSTUVWXYZABCDEFGHIJKLM"
    mapping = dict(zip(keys, vals))
    return mapping.get(char, char)

def is_even(num):
    return num % 2 == 0

def ask_for_password():
    return input("What's the password? ")

def ask_for_name():
    return input("What's your name? ")

words = ["aardvark", "table", "snowstorm", "periscope", "laminate"]
message = "JR NGGNPX NG QNJA"
number = 9
