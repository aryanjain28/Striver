#
# @lc app=leetcode id=908 lang=python
#
# [908] Smallest Range I
#

# @lc code=start
class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums = sorted(nums)
        if nums[0] + k >= nums[-1] - k:
            return 0
        return nums[-1] - nums[0] - 2*k


# @lc code=end
