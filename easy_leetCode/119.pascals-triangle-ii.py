#
# @lc app=leetcode id=119 lang=python
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        rowIndex += 2

        lastRow = [1, 1]
        row = 3
        while row < rowIndex:
            i = 1
            res = [1]
            while i < row - 1:
                res.append(lastRow[i] + lastRow[i-1])
                i += 1

            res += [1]
            lastRow = res
            row += 1

        return lastRow


# @lc code=end

print(Solution().getRow(2))
# print(Solution().getRow(3))
# print(Solution().getRow(4))
# print(Solution().getRow(5))
# print(Solution().getRow(6))
# print(Solution().getRow(7))
