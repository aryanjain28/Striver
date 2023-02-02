#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        p_start = -1
        p_end = -1
        max_len = 0

        reversed_s = s[::-1]
        res_str = ""

        i = 0
        j = 0

        dp = [[0 for i in range(len(s))] for j in range(len(reversed_s))]

        for i in range(len(s)):
            for j in range(len(reversed_s)):
                if s[i] == reversed_s[j]:
                    if (i == 0 or j == 0):
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1

                if dp[i][j] > max_len:
                    if i - dp[i][j] + 1 == len(reversed_s) - 1 - j:
                        # if s[i+1-dp[i][j]:i+1] == reversed_s[len(s) - dp[i][j]:j+1]:
                        p_end = i
                        max_len = dp[i][j]

        return s[p_end - max_len + 1: p_end + 1]

# abcdefcba
# abcfedcba


# @lc code=end
s = Solution()
print(s.longestPalindrome("abcdefcba"))
