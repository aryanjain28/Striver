#
# @lc app=leetcode id=567 lang=python
#
# [567] Permutation in String
#

# @lc code=start
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        LEN_S1 = len(s1)
        LEN_S2 = len(s2)

        if LEN_S1 > LEN_S2:
            return False

        s1Freq = [0]*26
        s2Freq = [0]*26

        for index in range(LEN_S1):
            s1Freq[ord(s1[index])-97] += 1
            s2Freq[ord(s2[index])-97] += 1

        if s1Freq == s2Freq:
            return True

        i = 0
        while i + LEN_S1 <= LEN_S2:
            if i + LEN_S1 >= LEN_S2:
                return False

            s2Freq[ord(s2[i+LEN_S1])-97] += 1
            s2Freq[ord(s2[i])-97] -= 1

            if s1Freq == s2Freq:
                return True

            i += 1

        return False


# @lc code=end
print(Solution().checkInclusion("a", "ab"))
