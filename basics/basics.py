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