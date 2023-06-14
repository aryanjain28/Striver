#
# @lc app=leetcode id=198 lang=python
#
# [198] House Robber
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        """

        if len(nums) == 1:
             return nums[0]

        r1 = nums[0]
        r2 = r1 if r1 > nums[1] else nums[1]
        for index in range(2, len(nums)):
                tmp = nums[index] + r1 if nums[index] + r1 > r2 else r2
                r1 = r2
                r2 = tmp

        return r2




        # cache = [0] * LEN
        # def rec(index):
        #     if cache[index] != 0:
        #         return cache[index]
 
        #     if index >= LEN - 2:
        #         return nums[index]
            
        #     local_max = -1
        #     for i in range(index+2, LEN):
        #         local_max = max(local_max, nums[index] + rec(i))

        #     cache[index] = local_max
        #     return local_max

        # return max(rec(0), rec(1))


            

        


        
# @lc code=end
print(Solution().rob([1,2,3,1]))
print(Solution().rob([2,7,9,3,1]))
print(Solution().rob([2,1,1,2]))
print(Solution().rob([1,2]))

