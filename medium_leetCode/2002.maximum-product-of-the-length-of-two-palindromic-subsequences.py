#
# @lc app=leetcode id=2002 lang=python
#
# [2002] Maximum Product of the Length of Two Palindromic Subsequences
#

# @lc code=start
class Solution(object):
    def maxProduct(self, s):
        """
        :type s: str
        :rtype: int
        """

        LEN = len(s)
        if LEN < 3:
            return 1

        mDict = {}
        for mask in range(1, 2**LEN):
            substring = ""
            for i in range(LEN):
                if mask & (1 << i):
                    substring += s[i]
            if substring == substring[::-1]:
                mDict[mask] = len(substring)

        product = 0
        for m1 in mDict:
            for m2 in mDict:
                if (m1 & m2) == 0:
                    product = max(product, mDict[m1]*mDict[m2])

        return product


# @lc code=end
Solution().maxProduct("ABA")
