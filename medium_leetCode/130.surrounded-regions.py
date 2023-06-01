#
# @lc app=leetcode id=130 lang=python
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        ROW_LEN = len(board)
        COL_LEN = len(board[0])

        def dfs(r, c):

            if r < 0 or r >= ROW_LEN or c < 0 or c >= COL_LEN or board[r][c] != "O":
                return

            board[r][c] = "#"

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
            
        # first and last row
        for c in range(COL_LEN):
            if board[0][c] == "O":
                dfs(0, c)
                
            if board[ROW_LEN-1][c] == "O":
                dfs(ROW_LEN-1, c)

    
        # first and last col
        for r in range(ROW_LEN):
            if board[r][0] == "O":
                dfs(r, 0)
                
            if board[r][COL_LEN-1] == "O":
                dfs(r,COL_LEN-1)


        for i in range(ROW_LEN):
            for j in range(COL_LEN):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
        
# @lc code=end
# Solution().solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
Solution().solve([["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]])
