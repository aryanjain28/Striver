#
# @lc app=leetcode id=153 lang=python
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        LEN = len(nums)
        if LEN == 1 or nums[0] < nums[-1]:
            return nums[0]

        i = 0
        j = LEN - 1
        min_ = float("inf")
        while i <= j:

            mid = (i + j) // 2

            min_ = min(nums[mid], min_)

            if nums[mid] < nums[j]:
                j = mid - 1
            else:
                i = mid + 1

        return min_

        # while i < j and nums[i] > nums[j]:
        #     i += 1
        #     j -= 1

        # if i == 0:
        #     return nums[0]
        # return min(nums[j+1], nums[i])


# @lc code=end
