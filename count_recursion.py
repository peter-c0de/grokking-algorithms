# Peter Ezzat
# Date: 7th November 2024

# Chapter 4: Quicksort
# Exercise: 4.2
# Page: 63

def count_items(arr):
    #if (arr==[]): return 0
    if not(arr): return 0
    return 1 + count_items(arr[1:])
  
arr1 = [1,2,3,4,5]
print( count_items(arr1) )