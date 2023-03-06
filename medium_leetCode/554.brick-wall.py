#
# @lc app=leetcode id=554 lang=python
#
# [554] Brick Wall
#

# @lc code=start
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """

        mDict = {}
        max_gap = 0
        for row in wall:
            gapIndex = 0
            for brick in row[:-1]:
                gapIndex += brick
                mDict[gapIndex] = mDict[gapIndex] + 1 if gapIndex in mDict else  1
                max_gap = max(max_gap, mDict[gapIndex])
        return len(wall) - max_gap


# @lc code=end
