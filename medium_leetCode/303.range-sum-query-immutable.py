#
# @lc app=leetcode id=303 lang=python
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        i = 1
        while i < len(nums):
            nums[i] += nums[i-1]
            i += 1
        self.nums = nums

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.nums[right] - (0 if left == 0 else self.nums[left - 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end
