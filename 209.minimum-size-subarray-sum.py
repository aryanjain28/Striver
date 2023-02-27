#
# @lc app=leetcode id=209 lang=python
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        numLen = 100001
        _sum = 0

        while j < len(nums):
            _sum += nums[j]
            while _sum >= target:
                numLen = min(j - i + 1, numLen)
                _sum -= nums[i]
                i += 1
            j += 1

        if numLen == 100001:
            return 0
        return numLen


# @lc code=end
print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(Solution().minSubArrayLen(4, [1, 4, 4]))
print(Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
print(Solution().minSubArrayLen(11, [1, 2, 3, 4, 5]))
