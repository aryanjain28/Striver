#
# @lc app=leetcode id=416 lang=python
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Memoization
        # cache = {}
        # def rec(s, index):

        #     if index >= len(nums) or s > SUM:
        #         return False
            
        #     if (s, index) in cache:
        #         return cache[(s, index)]
            
        #     if s == SUM:
        #         return True

        #     cache[(s, index)] = rec(s+nums[index], index + 1) or rec(s, index+1)
        #     return cache[(s, index)]
            

        # Memoization using set
        # target = sum(nums) / 2
        # mSet = set()
        # mSet.add(0)
        # for i in range(len(nums)):
        #     temp = set()
        #     for n in mSet:
        #         s = n + nums[i]
        #         # if s > target: 
        #         #     break
        #         if s == target:
        #             return True
        #         temp.add(s)
        #         temp.add(n)
        #     mSet = temp
        # return True if target in mSet else False

        # # Tabulation
        # SUM = sum(nums)
        # if SUM % 2 != 0:
        #     return False
        # SUM //= 2

        # N = len(nums)
        # M = SUM

        # matrix = [[True] * (M + 1) for _ in range(N+1)]
        # matrix[0] = [False] * (M + 1)
        # matrix[0][0] = True
        
        # nums = [-1] + nums
        # for i in range(1, N+1):
        #     for s in range(1, M+1):
        #         matrix[i][s] = matrix[i-1][s] or (matrix[i-1][s-nums[i]] if s >= nums[i] else False)

        # return matrix[-1][-1]

        # Tabulation - using less memory
        SUM = sum(nums)
        if SUM % 2 != 0:
            return False
        SUM //= 2

        N = len(nums)
        M = SUM

        r1 = [False] * (M + 1)
        r1[0] = True
        r2 = list(r1)
        
        nums = [-1] + nums
        for i in range(1, N+1):
            for s in range(1, M+1):
                r2[s] = r1[s] or (r1[s-nums[i]] if s >= nums[i] else False)
            r1 = list(r2)

        return r2[-1]









        
# @lc code=end
print(Solution().canPartition([2,2,1,1]))
# print(Solution().canPartition([1,2,5]))
# print(Solution().canPartition([2,3,7,8,10]))
# print(Solution().canPartition([1,5,11,5]))
# print(Solution().canPartition([1,2,3,5]))
# print(Solution().canPartition([89,49,21,31,74,56,34,23,35,15,74,59,75,47,16,81,1,32,42,75,4,3,54,55,95,65,10,90,15,23,19,30,24,91,3,84,11,76,6,96,78,84,58,80,28,96,11,46,36,84,3,14,32,86,67,8,60,70,65,57,63,15,61,79,66,55,92,44,62,76,19,52,59,72,2,60,75,52,37,100,1,92,1,40,11,68,61,22,88,70,50,82,81,39,80,75,67,31,3,55]))

