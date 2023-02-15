#
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        mDict = {}
        for n in nums:
            if n not in mDict:
                mDict[n] = 1
            else:
                del mDict[n]
        return list(mDict.keys())[0]


# @lc code=end
print(Solution().singleNumber([1]))
