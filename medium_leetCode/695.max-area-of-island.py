#
# @lc app=leetcode id=695 lang=python
#
# [695] Max Area of Island
#

# @lc code=start
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        def backtrack(r, c):

            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 0

            count = 1
            grid[r][c] = 0

            count += backtrack(r-1, c)
            count += backtrack(r+1, c)
            count += backtrack(r, c-1)
            count += backtrack(r, c+1)

            return count

        max_val = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_val = max(backtrack(i, j), max_val)

        return max_val


        
# @lc code=end

