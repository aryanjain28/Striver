#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        i = 0
        j = len(s) - 1
        while i <= j:
            left = str(s[i])
            right = str(s[j])
            if left.isalnum() and right.isalnum():
                if left.lower() == right.lower():
                    i += 1
                    j -= 1
                else:
                    return False
            else:
                if not left.isalnum():
                    i += 1
                if not right.isalnum():
                    j -= 1

        return True

        # def fun(c):
        #     return str(c).isalnum()

        # # _s = filter(str.isalnum, s) #[x if str.isalnum(x) else for x in s]
        # _s = list(filter(fun, s.strip()))
        # LEN = len(_s)
        # i = 0
        # for i in range(LEN):
        #     if _s[LEN - 1 - i].lower() != _s[i].lower():
        #         return False
        # return True


# @lc code=end
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
# print(Solution().isPalindrome("   4A man, a plan, a canal: Panama4   "))
print(Solution().isPalindrome(" race %^!@ car "))
