#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#

# @lc code=start
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # if len(nums) <= 1:
        #     return [[], [nums]]

        def backtrack(nums, temp, res):
            res.append(temp)
            for index in range(len(nums)):
                if index == 0 or nums[index-1] != nums[index]:
                    backtrack(nums[index+1:], temp+[nums[index]], res)
            return res

        nums.sort()
        return backtrack(nums, [], [])


# @lc code=end
Solution().subsetsWithDup([1, 2])
