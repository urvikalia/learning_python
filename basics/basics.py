# Day 1 - Basics of Python
var1 = 10 
var2 = "Hello, World!"
var3  = 3.14


print(var1)
print(var2)
print(var3)


var1 = str(var1)
print(var1)

try:
    var2 = int(var2)
    print(var2)
except ValueError:
    print(f"Cannot convert var2 ('{var2}') to an integer.")


var4 = int(var3)
print(var4)

print(bool(var1))
print(bool(var1))

var_name = input("Please enter your name... ")
print(var_name)
print("you have entered " + var_name)

print("Hello," + var_name + " how are you doing")

print("Hello, {} how are you doing".format(var_name))



num1 = 10
num2 = 20 

print("Addition is " , num1+num2)
print("Substraction is " , num1-num2)
if(num1>num2):
    print("num1 is greater than num2")
else:
    print("num2 is greater than num1")



int1 = int(input("please enter the first number: "))
int2 = int(input("please enter the second number: "))

print("addition is:", int1+int2)
print("multiplication is ", int1*int2)


#Day 2 - control flow   


num1 = int(input("Please enter the number: "))
if num1%2 ==0:
    print("Number is even")
else:
    print("Number is odd")



# for loop 
print("Printing 1to 5 using for loop")
for i in range(1, 6):
    print(i)


##while loop 
num1= 10
print("Printing numbers from 10 to 5 using while loop")
while(num1>5):
    print(num1)
    num1 =num1-1


# exception handling 
input_num = input("enter the number: ")
try:
    num1 = int(input_num)
    answer = num1/100
    answer =100/num1
    print("The answer is:", answer)
except ValueError:
    print("Invalid input, please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

