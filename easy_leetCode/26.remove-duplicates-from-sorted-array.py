#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return 1
        elif len(nums) == 2:
            if nums[0] != nums[1]:
                return 2
            return 1
        else:
            i = 1
            j = i + 1
            while j < len(nums):

                if i < len(nums) - 1:
                    if (nums[i] == nums[i+1] and nums[i] > nums[i-1]) or (nums[i] < nums[i+1] and nums[i] > nums[i-1]):
                        i += 1

                if nums[i] < nums[j] and j + 1 != i:
                    nums[i] = nums[j]
                    nums[i+1] = nums[j]
                    i += 1

                j += 1

            if i < len(nums):
                if nums[i-1] < nums[i]:
                    i += 1

            print(nums[:i])
            return i


# @lc code=end
s = Solution()

input_arr = [1, 1, 2]
output = s.removeDuplicates(input_arr)
print(output)

input_arr = [1, 2, 2, 2]
output = s.removeDuplicates(input_arr)
print(output)

input_arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
output = s.removeDuplicates(input_arr)
print(output)

input_arr = [1, 2, 3]
output = s.removeDuplicates(input_arr)
print(output)
