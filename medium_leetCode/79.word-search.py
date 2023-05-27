#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#

# @lc code=start
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        rows = len(board)
        cols = len(board[0])

        def backtrack(i, j, searchIndex):

            if searchIndex == len(word):
                return True

            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False

            elif board[i][j] == word[searchIndex]:

                temp = board[i][j]
                board[i][j] = ""

                res = backtrack(i-1, j, searchIndex+1) or \
                    backtrack(i+1, j, searchIndex+1) or \
                    backtrack(i, j+1, searchIndex+1) or \
                    backtrack(i, j-1, searchIndex+1)

                if not res:
                    board[i][j] = temp

                return res

            return False

        for m in range(rows):
            for n in range(cols):
                if board[m][n] == word[0] and backtrack(m, n, 0):
                    return True
        return False


# @lc code=end

print(Solution().exist(
    [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB"))

# print(Solution().exist([["A", "B", "C", "E"], [
#     "S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))
