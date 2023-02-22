#
# @lc app=leetcode id=205 lang=python
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        mDict1 = {}
        mDict2 = {}

        i = 0
        j = len(s) - 1

        while i <= j:
            if s[i] not in mDict1:
                mDict1[s[i]] = t[i]
            elif mDict1[s[i]] != t[i]:
                return False

            if t[i] not in mDict2:
                mDict2[t[i]] = s[i]
            elif mDict2[t[i]] != s[i]:
                return False

            if i != j:
                if s[j] not in mDict1:
                    mDict1[s[j]] = t[j]
                elif mDict1[s[j]] != t[j]:
                    return False

                if t[j] not in mDict2:
                    mDict2[t[j]] = s[j]
                elif mDict2[t[j]] != s[j]:
                    return False

            i += 1
            j -= 1

        return True


# @lc code=end
