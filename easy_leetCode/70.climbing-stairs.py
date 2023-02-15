#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#

# @lc code=start

import math


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        LEN = n
        res = 0
        n_one = n
        n_two = 0
        while True:

            # calculate
            res += math.comb(LEN, n_one)

            # even
            if n % 2 == 0:
                if n_one == 0:
                    return res
            # odd
            else:
                if n_one == 1:
                    return res

            n_one -= 2
            n_two += 1
            LEN -= 1


# @lc code=end
print(Solution().climbStairs(10))
