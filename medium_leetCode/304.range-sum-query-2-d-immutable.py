#
# @lc app=leetcode id=304 lang=python
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        new_row = []
        self.sum_matrix = []
        i = 0
        j = 0
        while i < len(matrix):
            j = 0
            row_sum = 0
            new_row = []
            while j < len(matrix[0]):
                row_sum += matrix[i][j]
                new_row.append(row_sum + (0 if i ==
                                          0 else self.sum_matrix[i-1][j]))
                j += 1
            self.sum_matrix.append(new_row)
            i += 1

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        return (
            self.sum_matrix[row2][col2]
            - (0 if row1 == 0 else self.sum_matrix[row1 - 1][col2])
            - (0 if col1 == 0 else self.sum_matrix[row2][col1 - 1])
            + (0 if row1 == 0 or col1 ==
               0 else self.sum_matrix[row1 - 1][col1 - 1])
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end
