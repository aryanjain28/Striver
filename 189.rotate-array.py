#
# @lc app=leetcode id=189 lang=python
#
# [189] Rotate Array
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        LEN = len(nums)

        if k % LEN == 0:
            print(nums)
            return nums

        iterations = max(LEN - k, k)
        for i in range(iterations):
            nums[i], nums[min(i+LEN-k, LEN-1)
                          ] = nums[min(i+LEN-k, LEN-1)], nums[i]
        print(nums)
        return nums


# @lc code=end

Solution().rotate([1, 2, 3, 4, 5], 2)
Solution().rotate([1, 2, 3, 4, 5], 3)


Solution().rotate([1, 2, 3, 4, 5, 6], 2)
