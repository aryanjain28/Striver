#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mDict = {}
        for n in nums:
            if n not in mDict:
                mDict[n] = 1
            else:
                return True
        return False
        
# @lc code=end

