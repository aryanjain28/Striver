#
# @lc app=leetcode id=448 lang=python
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for n in nums:
            n = abs(n)
            if nums[n - 1] > 0:
                nums[n - 1] = -nums[n - 1]
        return [i+1 for i in range(0, len(nums)) if nums[i] > 0]


# @lc code=end
