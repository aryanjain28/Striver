#
# @lc app=leetcode id=287 lang=python
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        mSet = set()
        for n in nums:
            if n in mSet:
                return n
            mSet.add(n)


# @lc code=end
