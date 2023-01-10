# O(n^3)
def maxSubArray_naive_approach(nums):
    maximum = nums[0]
    for i in range(0, len(nums)):
        j = len(nums)
        while j > i:
            curr_max = nums[i] + sum(nums[i+1:j])
            print(curr_max, nums[i], nums[i+1:j])
            if curr_max > maximum:
                maximum = curr_max
            j -= 1
    
    return maximum


# print(maxSubArray_naive_approach([5,4,-1,7,8]))


# O(n) - Kadane's Algorothm
def maxSubArray(nums):
    sum = 0
    maximum = nums[0]
    start = end = 0
    i = 0
    while i < len(nums):
        sum += nums[i]

        if sum > maximum:
            maximum = sum
            end = i

        if sum < 0:
            sum = 0
            start = i + 1

        i += 1
    return maximum, nums[start:end+1]


input_list = [5,4,-1,7,8]
maximum, list = maxSubArray(input_list)
print(maximum, list)