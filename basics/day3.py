#Day 3 : data structures 

lst = ["apple", "banana", "cherry"]
print(lst)
print("first element in the list is : ",lst[0])
print ("last element in the list is : ", lst[-1])


days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("Days of the week:", days_of_week)

# Accessing elements
print(days_of_week[0])  # First element
print(days_of_week[3])


# Slicing the list
print(days_of_week[1:7])
print(days_of_week[:3])  # First three elements
print(days_of_week[4:])  # Last three elements

#Dictionaries 
book ={
    "title" : "Order of time",
    "author" : "Carlo Rovelli",
    "year" : 2018
}

print(book)
print("Title of the book is :", book["title"])
print("Author of the book is :", book["author"])

for key, value in book.items():
    print(f"{key}: {value}")
# Adding a new key-value pair
book["publisher"] = "Penguin Random House"
print("Updated book dictionary:", book)

# Removing a key-value pair
del book["year"]
print("Book dictionary after deletion:", book)

print(book.keys())

print(book.items())

# Fetch all keys and print the length
keys = book.keys()
print("Number of keys in the book dictionary:", len(keys))

#checking if a key exists
if "year" in book.keys():
    print("year key is present in the book dictionary")
else:
    print("year key is not present in the book dictionary")

values = book.values()
print("Values are : ", values)


# A tuple is like a list but you can't change 
# its contents after creation

input_tuple = ("apple", "banana", "cherry")
print(input_tuple)
print("first element is: ", input_tuple[0])
print("last element in tuple is: ",input_tuple[-1])

## set is an unOrdered set of unique elements
input_set = {1,2,2,4,5,6,7,7,8,9,9}
print(input_set)
print(input_set.pop()) 
print(input_set.pop())
print(input_set.pop())  
print("Set after popping three elements:", input_set)


countries_wish_list= ("Cambodia","Thailand","Japan")
print("Countries in my wish list:",countries_wish_list)

input_set = {1,2,3,4,5,5,5,5,6}
print(input_set)