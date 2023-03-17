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
        k = k % LEN

        i = 0
        while i < LEN // 2:
            j = LEN - 1 - i
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

        i = 0
        while i < k // 2:
            j = k - 1 - i
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

        i = k
        j = LEN - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        # 2nd way.
        # LEN = len(nums)
        # k = k % LEN
        # if k == 0:
        #     return nums

        # for i, n in enumerate(nums[LEN-k:] + nums[:LEN-k]):
        #     nums[i] = n


# @lc code=end
