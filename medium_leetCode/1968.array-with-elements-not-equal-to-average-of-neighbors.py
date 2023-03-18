#
# @lc app=leetcode id=1968 lang=python
#
# [1968] Array With Elements Not Equal to Average of Neighbors
#

# @lc code=start
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        LEN = len(nums)
        i = 0
        j = (LEN // 2) + (0 if LEN % 2 == 0 else 1)
        lastIndex = 0
        nums = sorted(nums)
        res = []
        while lastIndex < LEN:
            if lastIndex % 2 == 0:
                res.append(nums[i])
                i += 1
            else:
                res.append(nums[j])
                j += 1
            lastIndex += 1
        return res


# @lc code=end
