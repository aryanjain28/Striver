#
# @lc app=leetcode id=80 lang=python
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 2
        j = 2
        while j < len(nums):
            if nums[j] > nums[i-2]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i


# @lc code=end
