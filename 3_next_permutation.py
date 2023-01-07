
def update_list(left_half, right_half):
    last_element = left_half[-1]
    next_lowest_index = 0

    for i in range(len(right_half)):
        if right_half[i] > last_element and right_half[i] < right_half[next_lowest_index]:
            next_lowest_index = i

    # swap
    temp = left_half[-1]
    left_half[-1] = right_half[next_lowest_index]
    right_half[next_lowest_index] = temp

    return left_half + sorted(right_half)

def next_permutation(list):
    i = len(list) - 1
    while i > 0:
        if i == 1 and list[i-1] > list[i]:
            return [i for i in reversed(list)]
        if list[i-1] < list[i]:
            return update_list(list[:i], list[i:])
        i -= 1

list = [1,2,3]
print(list)
print(next_permutation(list))