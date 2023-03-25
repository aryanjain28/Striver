#
# @lc app=leetcode id=875 lang=python
#
# [875] Koko Eating Bananas
#

# @lc code=start

import math


class Solution(object):

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        # i = 0
        # j = max(piles) - 1

        # res = float("inf")
        # while i <= j:
        #     mid = (i + j) // 2

        #     if sum([(math.ceil(n / (mid + 1))) for n in piles]) <= h:
        #         j = mid - 1
        #         res = min(res, mid + 1)
        #     else:
        #         i = mid + 1

        # return res

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if sum((pile - 1) / mid + 1 for pile in piles) <= h:
                right = mid
            else:
                left = mid + 1
        return left


# @lc code=end
