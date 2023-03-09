#
# @lc app=leetcode id=2017 lang=python
#
# [2017] Grid Game
#

# @lc code=start
class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        total_row_1 = sum(grid[0])
        row_sum_0 = total_row_1 - grid[0][0]
        row_sum_1 = 0
        robo2Max = max(row_sum_0, row_sum_1)
        min_ = robo2Max

        for col in range(1, len(grid[0])):
            grid[0][col] += grid[0][col-1]
            grid[1][col] += grid[1][col-1]
            row_sum_0 = total_row_1 - grid[0][col]
            row_sum_1 = grid[1][col-1]
            min_ = min(min_, max(row_sum_0, row_sum_1))

        return min_


# @lc code=end
