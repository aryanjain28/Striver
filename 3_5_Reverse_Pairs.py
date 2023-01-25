#
# @lc app=leetcode id=493 lang=python
#
# [493] Reverse Pairs
#

# @lc code=start
class Solution(object):
    def reversePairsBrute(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] > 2 * nums[j]:
                    count += 1

        return count

    count = 0
    def merge(self, left, right):

        res = []
        i = 0
        j = 0

        while(i < len(left) and j < len(right)):
            
            if left[i] < right[j]:
                res.append(right[j])
                j += 1                
            else:
                y = len(right) - 1
                while y >= 0 and left[i] > 2 * right[y]:
                    y -= 1
                    self.count += 1

                res.append(left[i])
                i += 1

        while i < len(left):
            res.append(left[i])
            i += 1

        while j < len(right):
            res.append(right[j])
            j += 1
            
        return res
        

    def merge_sort(self, nums):

        LEN = len(nums)

        if LEN <= 1:
            return nums

        midpoint = LEN // 2
        
        left = self.merge_sort(nums[:midpoint])
        right = self.merge_sort(nums[midpoint:])
        
        return self.merge(left, right)

    def reversePairs(self, nums):
        self.merge_sort(nums)
        return self.count

        # SORTED?  YES | NO

        # count = 0
        # count = 1
        # count = 2
        # count = 3

        # Using Merge Sort
        # [2 4 3 5 1]
        # [2 4] [3 5 1]
        # [2] [4] [3 5 1]
        # [2 4] [3] [5 1]
        # [2 4] [3] [5] [1]
        # [2 4] [3] [1 5]
        # [2 4] [1 3 5]
        # 
        
# @lc code=end
# s = Solution()
# print(s.merge_sort([2,4,3,5,1]))
# print(s.count)

# s1 = Solution()
# print(s1.merge_sort([1,3,2,3,1]))
# print(s1.count)

# s1 = Solution()
# input_arr = [3,2,1,4]
# print(input_arr)
# print(s1.merge_sort(input_arr))
# print(s1.count)

# s1 = Solution()
# input_arr = [-5,-5]
# print(input_arr)
# print(s1.merge_sort(input_arr))
# print(s1.count)

# print(s.reversePairsBrute([2,4,3,5,1]))
