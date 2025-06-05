# functions and modules 


# fucntions are block of code that are executed when called 

def greet():
    print("Hello, World!")


greet()

# Function with parameters
def add_numbers(num1,num2):
    return num1+num2

print("addition of 2 and 5 is: ",add_numbers(2,5))


# Function with default parameters
def add_numbers(num1,num2=10):
    return num1+ num2
    
print(add_numbers(5))


def add_numbers(num1, num2):
    sum =num1 + num2
    print(f"The sum of {num1} and {num2} is: {sum}")
    return sum

add_numbers(5, 15)  

#module is just a python file with reusable code 

# Importing a module

from random import randint

num1 = randint(1, 100) 
print("Generated random number is: ", num1) # Generates a random integer between 1 and 100

# file I/O operations
# Writing to a file
with open("output.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("This file contains some sample text.\n")


with open("output.txt", "r") as file:
    content = file.read()  # Read the entire file
    print(content)


with open("notes.txt", "w") as file:
    file.write("This is a sample note.\n")
    file.write("You can write multiple lines in this file.\n")

with open("notes.txt", "r") as file:
    lines = file.readlines()  # Read all lines into a list
    for line in lines:
        print(line.strip())  # Print each line without extra whitespace