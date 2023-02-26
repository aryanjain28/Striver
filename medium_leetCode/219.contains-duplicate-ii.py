#
# @lc app=leetcode id=219 lang=python
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mDict = {}
        for i, n in enumerate(nums):
            if n not in mDict:
                mDict[n] = i
            else:
                if abs(i - mDict[n]) <= k:
                    return True
                else:
                    mDict[n] = i
        return False

# @lc code=end
