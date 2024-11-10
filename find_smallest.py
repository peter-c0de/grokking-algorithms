# Peter Ezzat
# Date: 31st October 2024

# Chapter 2: Selection Sort
# Page: 38

def find_smallest(arr):
    smallest = arr[0]
    for i in range(1, len(arr)):
        if(arr[i]<smallest): smallest=arr[i]
    return(smallest)

print( find_smallest([7,1,3,2]) )
print( find_smallest([0,1,3,2]) )
print( find_smallest([7,1,3,-1]) )
print( find_smallest([700,1000,30000,100]) )