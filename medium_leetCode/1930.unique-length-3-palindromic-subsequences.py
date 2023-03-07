#
# @lc app=leetcode id=1930 lang=python
#
# [1930] Unique Length-3 Palindromic Subsequences
#

# @lc code=start
class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """

        counter = 0
        for c in set(s[::]):
            left = s.find(c)
            right = s.rfind(c)
            if left > -1:
                counter += len(set(s[left+1:right]))
        return counter


# @lc code=end
