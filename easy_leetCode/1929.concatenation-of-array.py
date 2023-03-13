#
# @lc app=leetcode id=1929 lang=python
#
# [1929] Concatenation of Array
#

# @lc code=start
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        LEN = len(nums)
        for i in range(LEN):
            nums.append(nums[i])
        return nums

# @lc code=end
