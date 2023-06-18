#
# @lc app=leetcode id=1143 lang=python
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        if text1 == text2:
            return len(text1)

        m = len(text1)
        n = len(text2)

        matrix = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                matrix[i][j] = matrix[i-1][j-1] + 1 if text1[i-1] == text2[j-1] else max(matrix[i-1][j], matrix[i][j-1])

        return matrix[-1][-1]


# @lc code=end
print(Solution().longestCommonSubsequence("bsbininm", "jmjkbkjkv"))

# print(Solution().longestCommonSubsequence("abcdaf", "acbcf"))
# print(Solution().longestCommonSubsequence("abcde", "ace"))
# print(Solution().longestCommonSubsequence("abc", "abc"))
# print(Solution().longestCommonSubsequence("abc", "def"))
