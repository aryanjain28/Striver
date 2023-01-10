# ignore
def is_sorted(list):
    for i in range(0,len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True

# main
def sort_0_1_2(nums):

    # 3 pointers
    traverse_pointer = 0
    left_pointer = 0
    right_pointer = len(nums) - 1

    while traverse_pointer <= right_pointer:

        if nums[traverse_pointer] == 2:
            # swap it with the right_pointer
            nums[traverse_pointer], nums[right_pointer] = nums[right_pointer], nums[traverse_pointer]
            right_pointer -= 1

        elif nums[traverse_pointer] == 0 and nums[left_pointer] != nums[traverse_pointer]: 
            # swap it with the left_pointer
            nums[traverse_pointer], nums[left_pointer] = nums[left_pointer], nums[traverse_pointer]
            left_pointer += 1
            traverse_pointer += 1

        elif nums[traverse_pointer] == 1:
            traverse_pointer += 1

    return nums

# sort_0_1_2([2,1,2,1,1,1])
# sort_0_1_2([2,1,2,2,2])
# sort_0_1_2([0,2,1])
# sort_0_1_2([0,2,2,2,0,2,1,1])
list = [1,0,1,2,2,0,0,0,2,0,1,0,0,1,0,2,0,0,0,1,1,0,2,1,1,2,1,0,1,2,2,2,0,0,2,0,1,0,1,1,0,0,1,2,1,2,2,2,0,0,0,2,0,1,1,2,1,2,0,2,2,2,2,0,0,1,1,1,2,2,2,0,0,1,2,0,1,2,2,2,0,1,2,1,0,1,1,1,1,1,0,1,1,0,2,2,2,1,1,1,1,0,1,2,2,2,0]
# list = [2,0,2,1,1,0]
sorted_list = sort_0_1_2(list)
print(sorted_list)
# print(is_sorted(sorted_list))

list2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1]
# sorted_list = sort_0_1_2(list2)
# print(is_sorted(sorted_list))

