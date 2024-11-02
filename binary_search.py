# Date: 31 October 2024
# Chapter 1: Introduction to Algorithms
# Page: 9

def binary_search(array, item):
    low = 0
    high = len(array)-1
    while(low<=high):
        mid = (low+high)//2
        if(array[mid]==item): return mid
        elif(item>array[mid]): low = mid+1
        else: high = mid-1
    return -1

print( binary_search([1,2,3], 1) )
print( binary_search([1,2,3], 2) )
print( binary_search([1,2,3], 3) )
print( binary_search([1,2,3], 0) )
print( binary_search([1,2,3], 4) )