#
# @lc app=leetcode id=229 lang=python
#
# [229] Majority Element II
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        elem1 = None
        elem2 = None

        c1 = 0
        c2 = 0

        for n in nums:
            if n == elem1:
                c1 += 1
            elif n == elem2:
                c2 += 1
            elif c1 == 0:
                elem1 = n
                c1 = 1
            elif c2 == 0:
                elem2 = n
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1

        c1 = 0
        c2 = 0
        for n in nums:
            if n == elem1:
                c1 += 1
            if n == elem2:
                c2 += 1

        result = []
        if c1 > len(nums) / 3:
            result.append(elem1)
        if c2 > len(nums) / 3:
            result.append(elem2)

        return result        

# @lc code=end
x = Solution()

input_arr = [1,2,2,3,2]
input_arr = [11,33,33,11,33,11]
input_arr = [1,2]
input_arr = [-1, -1, -1]
# input_arr = [2,2,2]
print(x.majorityElement(input_arr))

