#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 1
        right = x

        while left <= right:
            mid = left + (right - left) / 2

            if mid > x / mid:
                right = mid - 1
            elif mid < x / mid:
                left = mid + 1
            else:
                return mid

        print(int(right))
        return int(right)


# @lc code=end
print(Solution().mySqrt(8))
