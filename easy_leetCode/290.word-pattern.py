#
# @lc app=leetcode id=290 lang=python
#
# [290] Word Pattern
#

# @lc code=start
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """


        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        mDict = {}
        mSet = set()
        for i in range(0, len(pattern)):
            if pattern[i] not in mDict:
                if words[i] in mSet:
                    return False
                mDict[pattern[i]] = words[i]
                mSet.add(words[i])
            elif mDict[pattern[i]] != words[i]:
                return False

        return True


# @lc code=end
