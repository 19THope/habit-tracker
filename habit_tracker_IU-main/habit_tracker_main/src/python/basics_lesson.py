'''# Integer → whole number
age = 25
# Float → number with decimals
temperature = 36.6

# String → text, must be in quotes
name = "Alice"

# Boolean → True or False value
is_student = True

# Print values to the terminal
print("Name:", name)           # Outputs: Name: Alice
print("Temperature:", temperature)  # Outputs: Temperature: 36.6

import math
print(math.sqrt(16))  # Outputs: 4.0

import datetime
print(datetime.date.today())  # Outputs: today's date '''

'''
def check_age():
    age = int(input("Enter your age: "))

    if age < 18:
        print("You are a minor.")
    elif age == 18:
        print("You are exactly 18.")
    else:
        print("You are an adult.")

check_age() '''

'''def greet(name):
    print("Hello,", name)

user_name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age < 18:
        print("You are a minor.")
elif age == 18:
        print("You are exactly 18.")
else:
    greet(user_name)'''

x = 10
 
def print_local():
    x = 5  # Local variable inside function
    print("Inside function:", x)

#print_local()
print("Outside function:", x)


