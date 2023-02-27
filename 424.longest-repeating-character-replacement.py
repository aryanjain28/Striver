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
        mDict = {}
        res = 0

        while j < len(s):
            if s[j] not in mDict:
                mDict[s[j]] = 1
            else:
                mDict[s[j]] += 1
            if j - i + 1 - max(list(mDict.values())) <= k:
                res = max(j - i + 1, res)
                j += 1
            else:
                mDict[s[i]] -= 1
                mDict[s[j]] -= 1
                i += 1

        return res


# @lc code=end
print(Solution().characterReplacement("ABABBA", 2))
print(Solution().characterReplacement("AABABBA", 1))
