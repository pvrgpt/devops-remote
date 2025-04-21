#!/usr/bin/env python3

def print_separator(char='-'):
    print(char*40)

def greet(Uname):
    if not isinstance(Uname, str) or not Uname:
        print("Error: Invalid username provided.")
        return
    print(f"HEllo {Uname}, Welcome!")

def add_numbers(n1,n2):
    print(f"Adding {n1} and {n2}...")
    result = n1 + n2
    return result

print("Example 1: Simple Funtion call.")
print_separator()
print_separator('*')

print("\nExample 2: Function with a required arg.")
greet("Parth")
greet("Raja")
greet("")

print("\nExample 3: Function with multiple args and return value")
sum_result = add_numbers(45,76)
print(f"The sum is {sum_result}")

add_numbers(-10,35)
