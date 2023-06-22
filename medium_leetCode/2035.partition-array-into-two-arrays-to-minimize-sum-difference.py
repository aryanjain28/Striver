#
# @lc app=leetcode id=2035 lang=python
#
# [2035] Partition Array Into Two Arrays to Minimize Sum Difference
#

# @lc code=start
class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        total = sum(nums)


        R = len(nums)
        C = total // 2

        
        


        # r1 = [1] + [0] * C
        # r2 = r1[:]

        # for i in range(1, R+1):
        #     for j in range(C+1):
        #         r2[j] = r1[i-1]
        #         if j >= nums[i-1]:
        #             r2[j] += r1[j-nums[i-1]]
        #     r1 = r2[:]

        # print(r2)


        
# @lc code=end
Solution().minimumDifference([3,9,7,3])
