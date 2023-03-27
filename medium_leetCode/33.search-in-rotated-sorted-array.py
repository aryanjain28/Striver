#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 1st way
        
        i = 0
        j = len(nums) - 1
        min_value = float("inf")
        min_index = -1

        while i <= j:
            mid = (i + j) // 2

            if nums[mid] < min_value:
                min_value = nums[mid]
                min_index = mid

            if min_value < nums[j]:
                j = mid - 1
            else:
                i = mid + 1

        if target > nums[-1]:
            i = 0
            j = min_index - 1
        else:
            i = min_index
            j = len(nums) - 1

        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid

            if target < nums[mid]:
                j = mid - 1
            else:
                i = mid + 1

        return -1

        # 2nd way 

        # while i <= j:
        #     mid = (i + j) // 2
        #     if nums[mid] == target:
        #         return mid

        #     # left sorted portion
        #     if nums[i] <= nums[mid]:
        #         if target > nums[mid] or target < nums[i]:
        #             i = mid + 1
        #         else:
        #             j = mid - 1
        #     # right sorted portion
        #     else:
        #         if target < nums[mid] or target > nums[j]:
        #             j = mid - 1
        #         else:
        #             i = mid + 1
        # return -1
# @lc code=end
# print(Solution().search([4, 5, 6, 7, 0, 1, 2], 8))
# print(Solution().search([5, 1, 3], 5))
# print(Solution().search([4, 5, 6, 7, 8, 0, 2, 3], 8))
