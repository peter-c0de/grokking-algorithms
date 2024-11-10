# Peter Ezzat
# Date: 10th November 2024

# Chapter 4: Quicksort
# Exercise: 4.3
# Page: 63

def maximum(arr):
    if len(arr)==2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = maximum(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

print( maximum([1,2,5,1,2,4,7,1,2,3]) )