#
# @lc app=leetcode id=665 lang=python
#
# [665] Non-decreasing Array
#

# @lc code=start
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) < 2:
            return True

        i = 1
        count = 0
        while (i < len(nums)):
            if nums[i-1] > nums[i]:
                if count > 0:
                    return False
                min_val = min(nums[i], nums[i-1])
                if min_val >= (0 if i < 2 else nums[i-2]):
                    nums[i-1] = min_val
                else:
                    nums[i] = nums[i-1]
                count += 1
            i += 1
        return True

# @lc code=end
