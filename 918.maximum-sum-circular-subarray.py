#
# @lc app=leetcode id=918 lang=python
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        globalMax = nums[0]
        currMax = nums[0]
        globalMin = nums[0]
        currMin = nums[0]
        total = nums[0]

        for n in nums[1:]:
            total += n

            currMax = max(currMax + n, n)
            currMin = min(currMin + n, n)

            if globalMax < currMax:
                globalMax = currMax

            if globalMin > currMin:
                globalMin = currMin

        if globalMax < 0:
            return globalMax
        return max(total - globalMin, globalMax)


# @lc code=end
print(Solution().maxSubarraySumCircular([1, -2, 3, -2]))
print(Solution().maxSubarraySumCircular([5, -3, 5]))
print(Solution().maxSubarraySumCircular([-3, -2, -3]))
