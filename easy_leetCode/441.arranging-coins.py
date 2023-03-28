#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        # What is the max number of rows? w.r.t. n??? ANS: n;
        # If 10 coins, max rows = 10
        # If 5 coins, max rows = 5
        # If 3 coins, max rows = 3

        i = 1
        j = n

        while i <= j:
            mid = (i + j) // 2
            min_coins_req = mid * (mid + 1) // 2

            if min_coins_req > n:
                j = mid - 1
            elif min_coins_req < n:
                i = mid + 1
            else:
                return mid

        return j

        # O(n) solution

        # count = 1
        # num = 2
        # while True:
        #     if num >= n:
        #         return count

        #     num += (count + 2)
        #     count += 1


# @lc code=end
# print(Solution().arrangeCoins(6))
