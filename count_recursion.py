# Peter Ezzat Aziz
# Date: 7th November 2024

def count_items(arr):
    #if (arr==[]): return 0
    if not(arr): return 0
    return 1 + count_items(arr[1:])
  
arr1 = [1,2,3,4,5]
print( count_items(arr1) )