#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        i = 0
        j = len(arr)

        while i <= j:
            mid = (i + j) // 2

            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid

            elif arr[mid+1] < arr[mid]:
                j = mid - 1

            else:
                i = mid + 1

        return j


# @lc code=end
