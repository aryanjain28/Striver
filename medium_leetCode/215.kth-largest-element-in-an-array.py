#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq as hq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        return hq.nlargest(k, nums)[-1]
        
# @lc code=end

