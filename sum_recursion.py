# Peter Ezzat Aziz
# Date: 6th November 2024

### My Code ###
# Problem: Delete's the array
def sum(arr):
    if ( len(arr) == 1 ): return arr[0]
    return arr.pop() + sum(arr)

### Grokking Algorithms' Code ###
def sum(arr):
    if ( arr==[] ): return 0
    return arr[0] + sum(arr[1:])
  
arr1 = [1,2,3,4,5]
print(arr1)
print( sum(arr1) )
print(arr1)