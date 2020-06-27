# check if an array is sorted
def sorted(arr): 
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True


# elements at position a and b
def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a] 
    return arr


# return index of first element greater than the pivot
def goto_gt_pivot(arr, pivot, i = -1):
    for i in range(i + 1, len(arr)):
        if arr[i] > arr[pivot]:
            return i
    return 0


# return index of first element less than the pivot
def goto_lt_pivot(arr, pivot, beg_j):
    for j in range(beg_j - 1,  -1, -1):
        if arr[j] <= arr[pivot]:
            return j
    return 0
    

# recursively sort a given array
def quicksort(arr, pivot = 0):
    # no sorting to be done in either case
    if arr == [] or len(arr) == 1:
        return arr 
    # find first thing greater than pivot
    i = goto_gt_pivot(arr, pivot)
    # find first thing less than pivot
    j = goto_lt_pivot(arr, pivot, len(arr))
    
    while i < j:
        arr = swap(arr, i, j)
        i = goto_gt_pivot(arr, pivot, i)
        j = goto_lt_pivot(arr, pivot, j)
   
    # put the element at pivot in where j is
    # now, everything to the left of pivot is smaller and 
    # everything to the right is larger
    arr = swap(arr, j, pivot)
    pivot = j

    # recursively call quicksort on the left array and the right array
    arr[:pivot] = quicksort(arr[:pivot])
    arr[pivot + 1:] = quicksort(arr[pivot + 1:])

    return arr
