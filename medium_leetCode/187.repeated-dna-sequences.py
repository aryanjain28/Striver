#
# @lc app=leetcode id=187 lang=python
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        if len(s) < 10:
            return []

        mSet = set()
        seen = set()
        i = 0
        while i + 10 <= len(s):
            j = i + 10
            sub = s[i:j]
            if sub in seen:
                mSet.add(sub)
            seen.add(sub)
            i += 1

        return list(mSet)


# @lc code=end
