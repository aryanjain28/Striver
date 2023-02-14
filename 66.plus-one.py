#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
        else:
            digits[-1] = 0
            i = len(digits) - 2
            while i >= 0:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    return digits
                i -= 1

        return [1] + digits
        # return [int(s) for s in str(int("".join([str(i) for i in digits])) + 1)]


# @lc code=end
s = Solution()
print(s.plusOne([2, 3, 4, 5, 1, 9]))
print(s.plusOne([9]))
print(s.plusOne([2, 9, 9, 9]))
print(s.plusOne([9, 9, 9, 9]))
