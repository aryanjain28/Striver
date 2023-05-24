#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#

from itertools import combinations

# @lc code=start


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        return combinations(range(1, n+1), k)

        # res = []
        # def backtrack(combination, options):

        #     if len(combination) == k:
        #         res.append(combination)
        #         return

        #     for index, option in enumerate(options):
        #         backtrack(combination + [option], options[index+1:])

        #     return res

        # return backtrack([], list(range(1, n+1)))


# @lc code=end
Solution().combine(4, 2)
Solution().combine(1, 1)
