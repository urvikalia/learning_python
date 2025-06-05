# String manipulation 

text= "Hello, World!"

print(text.upper()) # Convert to uppercase
print(text.lower())  # Convert to lowercase
print(text.capitalize())



str = "   Uru is a good       girl     "
print(str.strip())

str= str.replace("good", "great") 
print(str)

# create list of first 10 numbers 

count =1
int_num=1 
lst=[]
while(count <=10):
    if(int_num %2 ==0):
        lst.append(int_num)
        count += 1
    int_num += 1

print("List of even numbers is :")
print(lst)
print(len(lst))



