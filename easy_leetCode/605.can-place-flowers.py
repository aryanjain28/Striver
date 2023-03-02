#
# @lc app=leetcode id=605 lang=python
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        LEN = len(flowerbed)
        if n == 0:
            return True
        if n > (LEN - (LEN // 2)):
            return False

        if LEN == 1:
            return (flowerbed[0] * n) == 0

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1

        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1

        i = 1
        while (i < LEN-1):
            if flowerbed[i] == 1:
                i += 2
                continue
            if flowerbed[i] + flowerbed[i-1] + flowerbed[i+1] == 0:
                n -= 1
                i += 1
            if n <= 0:
                return True
            i += 1
        return n <= 0


# @lc code=end
