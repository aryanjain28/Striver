#
# @lc app=leetcode id=213 lang=python
#
# [213] House Robber II
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def helper(nums):
            
            r1 = nums[0]
            r2 = r1 if r1 > nums[1] else nums[1]

            for index in range(2, len(nums)):
                tmp = nums[index] + r1 if nums[index] + r1 > r2 else r2
                r1 = r2
                r2 = tmp

            return r2

        if len(nums) <= 2:
            return nums[-1] if nums[-1] > nums[0] else nums[0]


        return max(
            helper(nums[:-1]),
            helper(nums[1:])
        )


        # h1 = helper(nums[:-1])
        # h2 = helper(nums[1:])
        # return h1 if h1 > h2 else h2
        
# @lc code=end
print(Solution().rob([2,3,2]))
print(Solution().rob([1,2,3,1]))
print(Solution().rob([1,2,3]))
print(Solution().rob([1,2,1,1]))
print(Solution().rob([200, 3, 140, 20, 10]))
print(Solution().rob([1]))

