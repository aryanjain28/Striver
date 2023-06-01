#
# @lc app=leetcode id=994 lang=python
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """     

        ROW_LEN = len(grid)
        COL_LEN = len(grid[0])
        
        freshC = 0
        queue = []

        for r in range(ROW_LEN):
            for c in range(COL_LEN):
                if grid[r][c] == 1:
                    freshC += 1
                if grid[r][c] == 2:
                    queue.append((r, c, 0))

        currTime = 0
        while queue:
            r, c, currTime = queue.pop(0)

            for (x,y) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if (0 <= r+x < ROW_LEN and 0 <= c+y < COL_LEN) and grid[r+x][c+y] == 1:
                    freshC -= 1
                    grid[r+x][c+y] = 2
                    queue.append((r+x, c+y, currTime+1))
            
            
        return currTime if freshC == 0 else -1


        
# @lc code=end
print(Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))

