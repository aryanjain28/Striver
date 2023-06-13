#
# @lc app=leetcode id=746 lang=python
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution(object):
    def minCostClimbingStairs(self, c):
        """
        :type c: List[int]
        :rtype: int
        """

        # Bottom Up
        fn1 = c[0]
        fn2 = c[1]
        for i in range(2, len(c)):
            temp = (fn1 if fn1 < fn2 else fn2) + c[i]
            fn1 = fn2
            fn2 = temp

        return min(fn1, fn2)
    



        # TOP DOWN APPROACH
        # def rec(i = 0):

        #     if i in cache:
        #         return cache[i]

        #     if i == len(c)-1 or i == len(c)-2:
        #         return c[i]
            
        #     cache[i] = min(minimum, min(c[i] + rec(i+1), c[i] + rec(i+2)))
        #     return cache[i]

        # return rec()

        
# @lc code=end
print(Solution().minCostClimbingStairs([10,15,20]))
print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
