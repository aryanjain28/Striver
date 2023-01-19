def majorityElement( nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    len_half = len(nums) // 2
    counter_dict = {}

    for n in nums:
        if n not in counter_dict:
            counter_dict[n] = 1
        else:
            counter_dict[n] += 1
        
        if counter_dict[n] > len_half:
            return n

def majority_element_balance(nums):
    balance = 1
    element = nums[0]

    for n in nums[1:]:
        if balance == 0:
            element = n

        if n != element:
            balance -= 1
        else:
            balance += 1
            
    return element

print(majorityElement([2,2,1,1,1,2,2]))
print(majority_element_balance([2,2,1,1,1,2,2]))

    