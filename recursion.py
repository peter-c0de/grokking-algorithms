# Peter Ezzat
# Date: 3rd November 2024

# Chapter 3: Recursion
# Page: 45

def countdown(i):
    print(i)
    countdown(i-1)

def countdown(i):
    print(i)
    if(i==1): return # Base Case
    countdown(i-1) # Recursive Case
    
countdown(10)
