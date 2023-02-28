#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        i = 0
        j = i + 2
        water = 0
        gap = 0
        remover = 0

        while j < len(height):

            hI = height[i]
            hJ = height[j]

            if hI > hJ or hI <= hJ:
                gap = j - i - 1
                waterArea = min(hI, hJ) * gap
                water = water + waterArea



            j += 1

# @lc code=end
