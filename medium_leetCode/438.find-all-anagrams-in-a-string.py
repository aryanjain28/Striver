#
# @lc app=leetcode id=438 lang=python
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        pLength = len(p)
        sLength = len(s)
        if pLength > sLength:
            return []

        res = []
        pDict = {}
        sDict = {}
        for i, c in enumerate(p):
            pDict[c] = pDict.get(c, 0) + 1
            sDict[s[i]] = sDict.get(s[i], 0) + 1

        for i in range(sLength - pLength + 1):
            if (sDict == pDict):
                res.append(i)
            sDict[s[i]] = sDict.get(s[i]) - 1
            if sDict[s[i]] <= 0:
                del sDict[s[i]]
            if i + pLength < sLength:
                sDict[s[i+pLength]] = sDict.get(s[i+pLength], 0) + 1

        return res


# @lc code=end
