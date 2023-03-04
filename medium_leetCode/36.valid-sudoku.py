#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        mSet = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if (board[i][j] + "R" + str(i) in mSet) or (board[i][j] + "C" + str(j) in mSet) or (board[i][j] + "B" + str(i//3) + "-" + str(j//3) in mSet):
                        return False
                    mSet.add(board[i][j] + "R" + str(i))
                    mSet.add(board[i][j] + "C" + str(j))
                    mSet.add(board[i][j] + "B" + str(i//3) + "-" + str(j//3))

        return True

# @lc code=end
