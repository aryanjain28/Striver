#
# @lc app=leetcode id=2001 lang=python3
#
# [2001] Smallest Missing Genetic Value in Each Subtree
#

# @lc code=start

class Solution(object):
    def interchangeableRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """

        from math import comb
        mDict = {}
        for w, h in rectangles:
            mDict[w/h] = 1 + mDict.get(w/h, 0)

        sum = 0
        for n in mDict.values():
            if n > 1:
                sum += comb(n, 2)
        return sum


# @lc code=end
