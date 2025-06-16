# Understanding functions in Python

# Notes 
# No type declaration , Python is dynamically typed
# Identation matters , no curly braces 
# def keyword instead of function 
# No explicity return type declaration 

import  json

def add(num1,num2):
    return num1 + num2


def subtract(num1,num2):
    return num1 -num2 


num1 = 12
num2 = 5 
print("addition is: " , add(num1,num2))
print("Sustraction is ", subtract(num1,num2))    


# Keyword arguments 

def create_api_endpoint(path="/users",method ="GET",auth_required=True,rate_limit=10):
    return {
        "path": path,
        "method": method,
        "auth_required": auth_required,
        "rate_limit": rate_limit
    }

#create default endpoint 
print("Endpoit created by default parameters: ")
print(create_api_endpoint())

#create custom endpoint 
print("Endpoint created by custom parameters: ")
print(create_api_endpoint("/products","POST",False,5))

print(type(create_api_endpoint()))

print("tinkering around return object of create_api_endpoint which is a dictionary")
api_endpoint_1 = create_api_endpoint("/products","POST",False,5)
api_endpoint_1.items()
copy_keys= api_endpoint_1.keys()
copy_values= api_endpoint_1.values()
api_endpoint_1.get("path")
print("lenght of api_endpoint_1 is: ", len(api_endpoint_1))
# Copying the dictionary
copy_endpoints = api_endpoint_1.popitem()

# print("keys are:",copy_keys)
# print("Values are:", copy_values)
# print(type(copy_keys))
# print(type(copy_values))

print("number of elements in endpoint dict: ",len(copy_endpoints))
print("printing poped items")
print(copy_endpoints)
print(type(copy_endpoints))

my_dict = {"name":"urvi","age":42,"is_student":False}
json_copy = json.dumps(my_dict)  # Convert dictionary to JSON string

# tuple 
# A tuple in python isan immutable sequence of values 
# immutable : once created , the elements of the tuple cannot be modified, added or removed
# The elements maintain their order and you can access tem using indexing 
# can contain mixed data type 
# tuples are created using paremtheses ()

my_tuple = (1, 2,3,"hello", "world", False, 3.14)
print("Tuple is: ", my_tuple)