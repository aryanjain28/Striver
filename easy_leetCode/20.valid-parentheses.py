#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 != 0:
            return False

        checked_arr = []

        i = 0
        while i < len(s):

            bracket = s[i]

            if bracket == "(" or bracket == "[" or bracket == "{":
                checked_arr.append(bracket)
            else:
                if len(checked_arr) < 1:
                    return False
                elif bracket == ")":
                    if not checked_arr.pop() == "(":
                        return False
                elif bracket == "]":
                    if not checked_arr.pop() == "[":
                        return False
                elif bracket == "}":
                    if not checked_arr.pop() == "{":
                        return False
            i += 1

        return not len(checked_arr) > 0


# @lc code=end


s = Solution()
print(s.isValid("([])"))
