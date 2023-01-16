def merge(left, right):
    i = j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1 

    while j < len(right):
        merged.append(right[j])
        j += 1
        
    return merged

def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    
    midpoint = len(arr) // 2
    left_arr = merge_sort(arr[:midpoint])
    right_arr = merge_sort(arr[midpoint:])

    sorted_arr = merge(left_arr, right_arr)

    return sorted_arr 


def find_duplicate_brute(arr):
    
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]

def find_duplicate_sorted(arr):
    sorted_arr = merge_sort(arr)
    for i in range(len(sorted_arr) - 1):
        if sorted_arr[i] == sorted_arr[i+1]:
            return sorted_arr[i]

def find_duplicate_frequency_arr(arr):
    f_arr = [0] * (len(arr) - 1)
    for n in arr:
        if f_arr[n-1] == 0:
            f_arr[n-1] = 1
        else:
            return n
# input_arr = [1,3,4,2,2]
input_arr = [1,3,4,3,2]
# output = find_duplicate_brute(input_arr)
output = find_duplicate_frequency_arr(input_arr)

print(output)