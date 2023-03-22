#
# @lc app=leetcode id=682 lang=python
#
# [682] Baseball Game
#

# @lc code=start
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        res = []
        for i in range(len(operations)):
            if operations[i] == "+":
                res.append(res[-1] + res[-2])
            elif operations[i] == "D":
                res.append(res[-1] * 2)
            elif operations[i] == "C":
                res.pop()
            else:
                res.append(int(operations[i]))

        return sum(res)


# @lc code=end
