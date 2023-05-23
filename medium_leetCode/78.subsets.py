#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def helper(numbers, temp=[], result=[]):
            result.append(list(temp))
            for index in range(len(numbers)):
                helper(numbers[index+1:], temp + [numbers[index]], result)

            return result
        return helper(nums)

        # iterative approach
        # I love this piece of code!!

        # using decision tree
        # subsets = []
        # LEN = len(nums)

        # def helper(root, index):
        #     if index >= LEN:
        #         subsets.append(root)
        #         return

        #     helper(root + [nums[index]], index + 1)  # including the element
        #     helper(root, index + 1)  # "not" including the element

        # helper([], 0)
        # return subsets
        # iterative approach
        # I love this piece of code!!

        # using decision tree
        # subsets = []
        # LEN = len(nums)

        # def helper(root, index):
        #     if index >= LEN:
        #         subsets.append(root)
        #         return

        #     helper(root + [nums[index]], index + 1)  # including the element
        #     helper(root, index + 1)  # "not" including the element

        # helper([], 0)
        # return subsets


# @lc code=end


Solution().subsets([1, 2, 3])
