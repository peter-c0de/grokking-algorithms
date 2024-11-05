# Date: 5th November 2024

# Factorial Recursion:
def factorial(i):
    if (i==1): return 1 # Base Case
    return i * factorial(i-1) # Recursive Case

print( factorial(3) )