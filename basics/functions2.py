# Advance functions
# variable arguments 

# write a function which takes variable arguments and returns a dictionary of results which performs basic functions 

def perform_stats(*args):
    if not args:
        return "No arguments provided."
    if not all(isinstance(args,(int,float)) for args in args):
        return "All arguments must be numbers."
    return {
        "max": max(args),
        "min": min(args),
        "count": len(args),
        "product": multiply(args)
    }



def multiply(numbers):
    result = 1
    for num in numbers:
        result = result * num
    return result


stat_output = perform_stats(1,2,3,4,5,6,7,8,9,10)

print(perform_stats())
print(perform_stats(1,2,"uhello","world"))


print(stat_output)

# kwargs keywords arguments 

def create_user_profile(name, email, **additional_info):
    profile = {
        "name": name,
        "email": email
    }
    profile.update(additional_info)
    return profile


user_profile = create_user_profile("Urvi","urvi@gmail.com",age=30,education="B.E.Computers")

print("User profile is as below")

print(user_profile)