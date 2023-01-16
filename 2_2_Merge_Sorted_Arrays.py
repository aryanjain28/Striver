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


def merge_sorted_arrays(arr1, arr2):
    i = 0
    j = i + 1
    k = 0

    while j < len(arr1):
        first = arr1[i]
        second = arr1[j]
        checkVal = arr2[k]
        swap_index = j + 1

        if first <= checkVal <=second:
            arr1[swap_index], arr2[k] = arr2[k], arr1[swap_index]
            arr1[swap_index], arr2[j] = arr2[j], arr1[swap_index]
            
            j += 1
            k += 1
        
        elif checkVal <= first:
            arr1[swap_index], arr2[k] = arr2[k], arr1[swap_index]
            arr1[swap_index], arr2[j] = arr2[j], arr1[swap_index]
            
            j += 1
            k += 1
        else:
            if checkVal > second:
                i += 1
                j += 1

    return


def merge(lArr, rArr):
    arr = []
    i = j = 0
    while i < len(lArr) and j < len(rArr) :

        if lArr[i] < rArr[j]:
            arr.append(lArr[i])
            i += 1

        else:
            arr.append(rArr[j])
            j += 1

    while i < len(lArr):
        arr.append(lArr[i])
        i += 1

    while j < len(rArr):
        arr.append(rArr[j])
        j += 1

    return arr

# Sort method for arr2
def merge_sort(arr):

    if len(arr) <= 1:
        return arr
 
    left_arr = merge_sort(arr[:(len(arr) // 2)])
    right_arr = merge_sort(arr[(len(arr) // 2):])

    return merge(left_arr, right_arr)


def merge_sorted_arrays_swap(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] = arr2[0], arr1[i]
            arr2 = merge_sort(arr2)

    return arr1 + arr2

input_arr_l = [1,4,8,10]
input_arr_r = [2,3,9]

input_arr_l = [1,2,3]
input_arr_r = [2,5,6]

print(input_arr_l, input_arr_r)

# arr1 = [1, 3, 5, 7]
# arr2 = [0, 2, 6, 8, 9]

# arr1 = [0, 1, 3]
# arr2 = [0, 1, 3]

# print(merge_sort([1,3,1,7,2,3]))
ouput_arr = merge_sorted_arrays_swap(input_arr_l, input_arr_r)

print(ouput_arr)

# print(merge_sorted_arrays_brute(arr1, arr2))