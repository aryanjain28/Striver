#
# @lc app=leetcode id=200 lang=python
#
# [200] Number of Islands
#

# @lc code=start
class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        R_LEN,  C_LEN = len(grid), len(grid[0])

        def backtrackNeighbours(r, c):

            grid[r][c] = "0"

            if r > 0 and grid[r-1][c] == "1":
                backtrackNeighbours(r-1, c)

            if r < R_LEN-1 and grid[r+1][c] == "1":
                backtrackNeighbours(r+1, c)

            if c > 0 and grid[r][c-1] == "1":
                backtrackNeighbours(r, c-1)

            if c < C_LEN-1 and grid[r][c+1] == "1":
                backtrackNeighbours(r, c+1)



        count = 0
        for i in range(R_LEN):
            for j in range(C_LEN):
                if grid[i][j] == "1":
                    count += 1 
                    backtrackNeighbours(i,j)

        return count




        
# @lc code=end
Solution().numIslands(
# [
#     ["1","1"],
#     ["1","1"]
# ]    
    
#     [
#     ["1","1","1","1","0"],
#     ["1","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
# ]

[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

)

