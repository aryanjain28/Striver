#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        LEN = len(nums)
        answer = [1] * LEN

        i = 0
        prefix = 1
        postfix = 1
        while i < LEN:
            answer[i] *= prefix
            prefix *= nums[i]
            answer[-1-i] *= postfix
            postfix *= nums[-1-i]
            i += 1
        return answer


# @lc code=end
Solution().productExceptSelf([1, 2, 3, 4])
