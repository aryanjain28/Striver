#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        fn1, fn2 = 1, 1
        for _ in range(2, n+1):
            fn1, fn2 = fn2, fn1 + fn2

        return fn2



        
# @lc code=end
Solution().climbStairs(6)

