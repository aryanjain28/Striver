#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        i = 0
        dp_arr = [0] * 26

        while i < len(s):

            dp_arr[ord(s[i]) - 97] += 1
            dp_arr[ord(t[i]) - 97] -= 1

            i += 1

        return len(set(dp_arr)) == 1


# @lc code=end
# Solution().isAnagram("aryan", "yanar")
# Solution().isAnagram("anagram", "nagaram")
# print(Solution().isAnagram("aacc", "ccac"))
# print(Solution().isAnagram("dgqztusjuu", "dqugjzutsu"))
# print(Solution().isAnagram("rat", "car"))
