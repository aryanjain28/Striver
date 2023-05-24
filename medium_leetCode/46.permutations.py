#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#

from itertools import permutations

# @lc code=start


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


        # res = []
        # LEN = len(nums)

        # def backtrack(options, perm):
        #     if len(perm) == LEN:
        #         res.append(perm)
        #         return
        #     for i in range(len(options)):
        #         backtrack(options[:i]+options[i+1:], perm + [options[i]])
        #     return res

        # return backtrack(nums, [])

        return permutations(nums, len(nums))
# @lc code=end


print(Solution().permute([1, 2, 3]))
