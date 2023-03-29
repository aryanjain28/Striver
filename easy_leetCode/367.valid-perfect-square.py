#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        i = 0
        j = num

        while i <= j:
            mid = (i+j) // 2

            if mid ** 2 == num:
                return True

            if mid ** 2 > num:
                j = mid - 1
            else:
                i = mid + 1

        return False

        # num **= (1/2)
        # return int(num) == num


# @lc code=end
# print(Solution().isPerfectSquare(14))
