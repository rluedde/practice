def compute_diff(arr1, arr2):
    diff = 0
    if len(arr1) != len(arr2):
        return -1
    else:
        for i in range(len(arr1)):
            diff += abs(arr1[i] - arr2[i])
    return diff

# Assume arrays are same lenght - no need to check
def rec_compute_diff(arr1, arr2, i = 0, diff = 0):
    if i >= len(arr1):
        return diff

    diff += abs(arr1[i] - arr2[i])
    return rec_compute_diff(arr1, arr2, i + 1, diff)

# Should return 8
arr1 = [10, 12, 14, 1, 6, 9]
arr2 = [9, 14, 13, 3, 8, 10]

iterative =  compute_diff(arr1, arr2)
recursive = rec_compute_diff(arr1, arr2)
print("it: ",iterative,"rec: ", recursive)
assert iterative == recursive
