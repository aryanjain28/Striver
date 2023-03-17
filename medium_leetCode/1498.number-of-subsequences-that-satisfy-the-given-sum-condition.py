#
# @lc app=leetcode id=1498 lang=python
#
# [1498] Number of Subsequences That Satisfy the Given Sum Condition
#

# @lc code=start
class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        count = 0
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                count += pow(2, j-i, 10**9+7)
                i += 1

        return count % (10**9 + 7)


# @lc code=end
