#
# @lc app=leetcode id=680 lang=python
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s_rev = s[::-1]
        if s_rev == s:
            return True

        i = 0
        j = len(s) - 1

        while i < j:
            # print(i, j, s[i], s[j])
            # print(s[i:j], s[i:j][::-1])
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif j-i <= 1:
                return True
            elif s[i+1:j+1] == s[i+1:j+1][::-1]:  # s[j+1:i:-1]:
                return True
            elif s[i:j] == s[i:j][::-1]:  # s[j-1:i+1:-1]:
                return True
            else:
                return False

        return False


# @lc code=end
print(Solution().validPalindrome("abc"))
# print(Solution().validPalindrome("abbabaa"))
