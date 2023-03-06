#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) <= 1:
            return 0

        min_price = prices[0]
        profit = 0
        i = 0
        while i < len(prices):
            if prices[i] < min_price:
                min_price = prices[i]
            if profit < prices[i] - min_price:
                profit = prices[i] - min_price
            i += 1
        return profit


# @lc code=end
print(Solution().maxProfit([2, 4, 1]))
