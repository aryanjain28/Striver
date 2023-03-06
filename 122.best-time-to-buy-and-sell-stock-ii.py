#
# @lc app=leetcode id=122 lang=python
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0
        i = 1
        while i < len(prices):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
            i += 1
        return profit


# @lc code=end
