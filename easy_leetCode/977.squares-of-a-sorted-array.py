#
# @lc app=leetcode id=977 lang=python
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # First finding mid-point, then traversing.
        
        # if nums[0] > 0:
        #     return [n**2 for n in nums]

        # if nums[-1] < 0:
        #     nums = [n**2 for n in nums]
        #     nums.reverse()
        #     return nums

        # i = 0
        # j = len(nums) - 1

        # while True:
        #     mid = (i + j) // 2
        #     if nums[mid] >= 0:
        #         j = mid
        #     elif nums[mid] < 0:
        #         i = mid + 1

        #     if i == j:
        #         mid = j
        #         break

        # if abs(nums[mid-1]) < abs(nums[mid]):
        #     mid -= 1

        # res = [nums[mid] ** 2]

        # i = mid - 1
        # j = mid + 1

        # while i >= 0 and j < len(nums):
        #     if abs(nums[i]) < abs(nums[j]):
        #         res.append(nums[i] ** 2)
        #         i -= 1
        #     else:
        #         res.append(nums[j] ** 2)
        #         j += 1

        # while i >= 0:
        #     res.append(nums[i] ** 2)
        #     i -= 1

        # if j < len(nums):
        #     res.extend([n ** 2 for n in nums[j:]])

        # return res


# @lc code=end
