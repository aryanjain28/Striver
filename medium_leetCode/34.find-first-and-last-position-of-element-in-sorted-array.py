#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution(object):

    def bin_search(self, nums, target, type):

        i = 0
        j = len(nums) - 1

        ans = -1
        while i <= j:
            mid = (i + j) // 2

            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                ans = mid
                if type < 0:
                    j = mid - 1
                else:
                    i = mid + 1

        return ans

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        return [self.bin_search(nums, target, -1),
                self.bin_search(nums, target, 1)]


# @lc code=end
