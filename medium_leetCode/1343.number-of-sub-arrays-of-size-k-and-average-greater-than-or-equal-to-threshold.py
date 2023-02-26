#
# @lc app=leetcode id=1343 lang=python
#
# [1343] Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
#

# @lc code=start
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """

        i = 0
        count = 0
        arr_sum = sum(arr[:k])

        while i <= len(arr) - k:
            if arr_sum / k >= threshold:
                count += 1
            i += 1
            if i+k-1 < len(arr):
                arr_sum += - arr[i - 1] + arr[i + k - 1]

        return count


# @lc code=end
# print(Solution().numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))
print(Solution().numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))
