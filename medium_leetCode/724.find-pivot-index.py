#
# @lc app=leetcode id=724 lang=python
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = sum(nums)

        for i, n in enumerate(nums):
            right -= n
            if left == right:
                return i
            left += n

        # sum_nums = [nums[0]]
        # while i < len(nums):
        #     sum_nums.append(sum_nums[i-1] + nums[i])
        #     i += 1

        # i = 0
        # while i < len(nums):
        #     left = 0 if i == 0 else sum_nums[i-1]
        #     right = 0 if i == len(nums) - 1 else sum_nums[-1] - nums[i] - left
        #     if left == right:
        #         return i
        #     i += 1
        return -1


# @lc code=end
