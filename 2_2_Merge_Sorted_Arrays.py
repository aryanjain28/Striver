def merge_sorted_arrays_brute(arr1, arr2):
    arr = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):

        first = arr1[i]
        second = arr2[j]

        if first < second and i < len(arr1):
            arr.append(first)
            i += 1
        elif second < first and j < len(arr2):
            arr.append(second) 
            j += 1
        elif first == second:
            arr.append(first)
            arr.append(second)
            i += 1
            j += 1

    if i < len(arr1):
        arr = arr + arr1[i:]
    if j < len(arr2):
        arr = arr + arr2[j:]

    return arr[:len(arr1)], arr[len(arr1):]

arr1 = [1,4,8,10]
arr2 = [2,3,9]

# arr1 = [1, 3, 5, 7]
# arr2 = [0, 2, 6, 8, 9]

# arr1 = [0, 1, 3]
# arr2 = [0, 1, 3]

print(merge_sorted_arrays_brute(arr1, arr2))