#
# @lc app=leetcode id=523 lang=python
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        mDict = {0: -1}
        sum_ = 0

        for i, n in enumerate(nums):
            sum_ += n
            remainder = sum_ % k
            if remainder not in mDict:
                mDict[remainder] = i
            elif (i - mDict[remainder] >= 2):
                return True

        return False


# @lc code=end
