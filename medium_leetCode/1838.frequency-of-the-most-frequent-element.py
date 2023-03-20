#
# @lc app=leetcode id=1838 lang=python
#
# [1838] Frequency of the Most Frequent Element
#

# @lc code=start
class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums.sort()
        i = 0
        for j in range(len(nums)):
            k += nums[j]
            if k < nums[j] * (j - i + 1):
                k -= nums[i]
                i += 1
        return j - i + 1


# @lc code=end
