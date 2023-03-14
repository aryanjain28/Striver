#
# @lc app=leetcode id=1984 lang=python
#
# [1984] Minimum Difference Between Highest and Lowest of K Scores
#

# @lc code=start
class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums = sorted(nums, reverse=True)
        res = nums[0]
        for i in range(len(nums) - k + 1):
            res = min(res, nums[i] - nums[i + k - 1])
        return res


# @lc code=end
