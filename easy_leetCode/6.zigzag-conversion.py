#
# @lc app=leetcode id=6 lang=python
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1 or len(s) <= numRows:
            return s

        currRow = 0
        res = ""
        charsInSec = (2*numRows) - 2

        while currRow < numRows:
            k = currRow
            while k < len(s):
                res += s[k]
                if currRow != 0 and currRow != numRows - 1:
                    charInBetween = charsInSec - 2 * currRow
                    if k + charInBetween < len(s):
                        res += s[k + charInBetween]
                k += charsInSec
            currRow += 1
        return res


# @lc code=end
Solution().convert("PAYPALISHIRING", 3)
Solution().convert("PAYPALISHIRING", 4)
Solution().convert("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5)
