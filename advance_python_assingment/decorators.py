# Create a decorator function to check that the argument passed to the function factorial is a non-negative integer:

# Create a factorial function which finds the factorial of a number.

# Use the decorator to decorate the factorial function to only allow factorial of non-negative integers.

# example: 

#     factorial(1.354) : raise Exception or print error message
#     factorial(-1) : raise Exception or print error message
#     factorial(5) : 60

def validate_input(func):
    def wrapper(n):
        if not isinstance(n, int):
            raise ValueError("Input must be an integer")
        
        if n < 0:
            raise ValueError("Input must be a non-negative integer")
    
        return func(n)
    return wrapper

@validate_input
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))      
print(factorial(0))      

# Wrong inputs
print(factorial(-1))    
print(factorial(1.354))
    