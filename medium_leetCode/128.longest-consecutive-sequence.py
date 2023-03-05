#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = set(nums)
        currCount = 0
        best = 0
        for n in nums:
            currCount = 0
            if n - 1 not in nums:
                currCount = 1
                while n + 1 in nums:
                    currCount += 1
                    n += 1
            best = max(currCount, best)
        return best


# @lc code=end
