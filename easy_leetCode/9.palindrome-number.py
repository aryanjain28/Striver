#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0: return False
        if 0 <= x < 10 : return True

        # y = 0
        # multiplier = 1
        # for str_n in str(x):
        #     y += (multiplier * int(str_n))
        #     multiplier *= 10

        return x-int(str(x)[::-1]) == 0 
        # return x-int(''.join(reversed(str(x)))) == 0 
        



# @lc code=end
s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(0))
print(s.isPalindrome(101))

