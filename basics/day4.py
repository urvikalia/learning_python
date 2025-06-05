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