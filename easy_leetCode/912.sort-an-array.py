#
# @lc app=leetcode id=912 lang=python
#
# [912] Sort an Array
#

# @lc code=start
class Solution(object):

    # def merge(self, left, right):
    #     merged = []
    #     i = 0
    #     j = 0

    #     while i < len(left) and j < len(right):
    #         if left[i] < right[j]:
    #             merged.append(left[i])
    #             i += 1
    #         else:
    #             merged.append(right[j])
    #             j += 1

    #     if i < len(left):
    #         merged.extend(left[i:])

    #     if j < len(right):
    #         merged.extend(right[j:])

    #     return merged

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(nums)
        # LEN = len(nums)
        # if LEN <= 1:
        #     return nums

        # left = self.sortArray(nums[:(LEN // 2)])
        # right = self.sortArray(nums[(LEN // 2):])

        # return self.merge(left, right)


# @lc code=end
