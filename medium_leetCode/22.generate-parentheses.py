#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ans = []

        def combinations(temp=[], open=0, close=0):
            if len(temp) == 2 * n:
                ans.append("".join(temp))
                return
            if open < n:
                temp.append("(")
                combinations(temp, open+1, close)
                temp.pop()
            if open > close:
                temp.append(")")
                combinations(temp, open, close+1)
                temp.pop()

        combinations()
        return ans


# @lc code=end
# print(Solution().generateParenthesis(1))
# print(Solution().generateParenthesis(2))
# print(Solution().generateParenthesis(3))
# print(Solution().generateParenthesis(4))
