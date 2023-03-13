#
# @lc app=leetcode id=344 lang=python
#
# [344] Reverse String
#

# @lc code=start
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        LEN = len(s)
        for i in range(LEN // 2):
            s[i], s[LEN-1-i] = s[LEN-1-i], s[i]
        return s


# @lc code=end
print(Solution().reverseString(["h", "e", "l", "l", "o"]))
