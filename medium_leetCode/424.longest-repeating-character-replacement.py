#
# @lc app=leetcode id=424 lang=python
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        i = 0
        j = 0
        mArr = [0] * 26
        res = 0

        while j < len(s):
            mArr[ord(s[j]) - 65] += 1
            if j - i + 1 - max(mArr) <= k:
                res = max(j - i + 1, res)
                j += 1
            else:
                mArr[ord(s[i]) - 65] -= 1
                mArr[ord(s[j]) - 65] -= 1
                i += 1

        return res


# @lc code=end
print(Solution().characterReplacement("ABABBA", 2))
print(Solution().characterReplacement("AABABBA", 1))
