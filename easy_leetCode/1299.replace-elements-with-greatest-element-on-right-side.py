#
# @lc app=leetcode id=1299 lang=python
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        maxSoFar = arr[-1]
        arr[-1] = -1
        i = len(arr) - 1 - 1
        while i >= 0:
            n = arr[i]
            arr[i], maxSoFar = maxSoFar, max(n, maxSoFar)
            i -= 1
        return arr


# @lc code=end
