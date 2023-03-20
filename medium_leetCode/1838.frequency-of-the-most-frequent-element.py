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
        j = 0
        total = 0
        windowLen = -1

        while j < len(nums):
            total += nums[j]
            while k + total < nums[j] * (j - i + 1):
                total -= nums[i]
                i += 1

            windowLen = max(windowLen, j - i + 1)
            j += 1

        return windowLen

        # for j in range(len(nums)):
        #     k += nums[j]
        #     if k < nums[j] * (j - i + 1):
        #         k -= nums[i]
        #         i += 1
        # return j - i + 1


# @lc code=end
Solution().maxFrequency([1, 2, 4], 5)
