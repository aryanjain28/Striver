#
# @lc app=leetcode id=374 lang=python
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        min_ = 1
        max_ = n
        while True:
            num = (min_ + max_) // 2
            result = guess(num)

            if result == 0:
                return num
            elif result == -1:
                max_ = num - 1
            else:
                min_ = num + 1


# @lc code=end
