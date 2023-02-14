#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#

# @lc code=start
class Solution(object):

    def binary_search(self, nums, target):
        i = 0
        j = len(nums) - 1

        if target < nums[0]:
            return i
        elif target > nums[-1]:
            return len(nums)

        midpoint = (i+j) // 2
        while (i <= j):
            midpoint = (i+j) // 2

            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                j = midpoint - 1
            else:
                i = midpoint + 1

        return i

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary_search(nums, target)


# @lc code=end
s = Solution()
o = s.searchInsert([1, 2, 4, 5], 3)
print(o)
