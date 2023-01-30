#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):

    def binary_search(self, nums, target):

        i = 0
        j = len(nums) - 1

        while i < j:
            mid = (i + j) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                i = mid + 1
            else:
                j = mid - 1

        return -1

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        


# @lc code=end
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([15, 51, 2, 7, 11], 11))
