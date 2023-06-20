#
# @lc app=leetcode id=494 lang=python
#
# [494] Target Sum
#

# @lc code=start
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        s = sum(nums) + target
        if s < 0 or s % 2:
            return 0

        s //= 2        
        r1 = [1] + [0]*s
        r2 = r1[:]

        for i in range(1, len(nums)+1):
            for j in range(s+1):
                r2[j] = r1[j] + (r1[j-nums[i-1]] if nums[i-1] <= j else 0)
            
            r1 = r2[:]

        return r2[-1]



        
# @lc code=end

# print(Solution().findTargetSumWays([1,1,1,1,1], 3))
# print(Solution().findTargetSumWays([1], 1))
print(Solution().findTargetSumWays([0,0,0,0,0,0,0,0,1], 1))