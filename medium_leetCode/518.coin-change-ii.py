#
# @lc app=leetcode id=518 lang=python
#
# [518] Coin Change II
#

# @lc code=start
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        T = [0]*(amount+1)        
        T[0] = 1
        for coin in coins:
            for cap in range(coin, amount+1):
                T[cap] = T[cap] + T[cap-coin]

        return T[-1]




        
# @lc code=end
Solution().change(5, [1, 2, 5])

