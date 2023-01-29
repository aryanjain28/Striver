#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0

        i = 0
        j = i + 1
        ans = s[0]

        while i < len(s) and j < len(s):

            string = s[i:j+1]

            if s[j] in string[:-1]:
                i += 1
            else:
                if len(string) > len(ans):
                    ans = string
                j += 1

        return len(ans)


# @lc code=end
s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("dvdf"))
