#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        mDict = {}
        for i, n in enumerate(numbers):
            if n in mDict:
                if i+1 > mDict[n]+1:
                    return [mDict[n]+1, i+1]
                return [i+1, mDict[n]+1]
            mDict[target-n] = i

# @lc code=end
