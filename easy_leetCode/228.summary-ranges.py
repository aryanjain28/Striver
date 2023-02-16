#
# @lc app=leetcode id=228 lang=python
#
# [228] Summary Ranges
#

# @lc code=start
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        if len(nums) < 1:
            return []

        k = 0
        res = [str(nums[k])]
        i = 1
        while i < len(nums):
            if nums[i] - 1 == nums[i-1]:
                res[-1] = str(nums[k]) + "->" + str(nums[i])
            else:
                res.append(str(nums[i]))
                k = i
            i += 1

        return res

# @lc code=end
