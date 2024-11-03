# Basic Recursion:

def countdown(i):
    print(i)
    countdown(i-1)

def countdown(i):
    print(i)
    if(i==1): return # Base Case
    countdown(i-1) # Recursive Case
    
countdown(10)
