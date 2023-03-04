#
# @lc app=leetcode id=1189 lang=python
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """

        if len(text) < 7:
            return 0

        result = [0] * 5
        for c in text:
            if ord(c)-97 in [0, 1, 11, 13, 14]:
                if ord(c)-97 <= 11:
                    result[min(2, ord(c)-97)] += 1
                else:
                    result[ord(c)-97-10] += 1

        result[2] //= 2
        result[4] //= 2
        return min(result)

# @lc code=end
