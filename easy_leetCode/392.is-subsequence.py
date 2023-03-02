#
# @lc app=leetcode id=392 lang=python
#
# [392] Is Subsequence
#

# @lc code=start
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        LEN = len(s)
        if LEN > len(t):
            return False
        if LEN == 0:
            return True

        i = 0
        for c in t:
            if c == s[i]:
                i += 1
            if i == LEN:
                return True
        return False


# @lc code=end
