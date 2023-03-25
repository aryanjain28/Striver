#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution(object):

    def bin_search(self, matrix, target):

        i = 0
        while i < len(matrix):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                break
            i += 1

        if i >= len(matrix):
            return False

        try:
            matrix[i].index(target)
            return True
        except:
            return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        return self.bin_search(matrix, target)


# @lc code=end
