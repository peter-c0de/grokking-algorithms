# Peter Ezzat
# Date: 31st October 2024

# Chapter 2: Selection Sort
# Page: 38

def find_smallest(arr):
    smallest = 0
    for i in range( 1,len(arr) ):
        if ( arr[i]<arr[smallest] ): smallest = i
    return smallest

def selection_sort(arr):
    array_sorted = []
    while(arr):
        smallest = arr.pop( find_smallest(arr) )
        array_sorted.append( smallest )
    return array_sorted

#print( find_smallest([7,1,3,2]) )
#print( find_smallest([0,1,3,2]) )
#print( find_smallest([7,1,3,0]) )
print( selection_sort([7,3,2]) )
print( selection_sort([7,1,3,2,10,-1]) )
print( selection_sort([0,7,1,3,2,10,-1]) )

print("\n\n")
