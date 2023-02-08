#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        mDict = {}

        for i, n in enumerate(nums):
            if n in mDict:
                return [i, mDict[n]]
            mDict[target - n] = i


# @lc code=end
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([15, 51, 2, 7, 11], 11))
