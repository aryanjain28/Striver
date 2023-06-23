#
# @lc app=leetcode id=322 lang=python
#
# [322] Coin Change
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, capacity):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if capacity == 0:
            return 0
        
        T = [capacity + 1] * (capacity + 1)
        T[0] = 0
        for i in range(1, len(coins)+1):
            for cap in range(1, capacity + 1):
                if cap >= coins[i-1]:
                    T[cap] = min(T[cap], 1 + T[cap-coins[i-1]])

        return -1 if T[-1] > capacity else T[-1]
            
        


        
# @lc code=end
Solution().coinChange([1,2,5], 11)
Solution().coinChange([2], 3)
Solution().coinChange([1], 0)
