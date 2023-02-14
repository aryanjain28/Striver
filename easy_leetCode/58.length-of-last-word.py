#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        lastI = -1
        lastJ = -1
        while i < len(s):
            if s[i] != " ":

                if lastJ + 1 < i:
                    lastI = -1

                lastJ = i

                if lastI < 0:
                    lastI = i
            i += 1

        return lastJ - lastI + 1
        # return len(s.split()[-1])


# @lc code=end
s = Solution()
print(s.lengthOfLastWord("    fly   me   to   the moon   "))
print(s.lengthOfLastWord("aryan"))
print(s.lengthOfLastWord("ary    an"))
