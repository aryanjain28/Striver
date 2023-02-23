#
# @lc app=leetcode id=168 lang=python
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution(object):
    def convertToTitle(self, n):
        """
        :type columnNumber: int
        :rtype: str
        """
        
        res = ""
        while n > 0:
            remainder = n % 26
            if remainder == 0:
                remainder = 26
            res = chr(64 + remainder) + res
            n = (n - remainder) // 26

        return res


# @lc code=end
print(Solution().convertToTitle(28))
print(Solution().convertToTitle(26*27 + 1))
# print(Solution().convertToTitle(701))
