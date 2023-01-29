#
# @lc app=leetcode id=18 lang=python
#
# [18] 4Sum
#

# @lc code=start
class Solution(object):

    def merge(self, left, right):

        i = 0
        j = 0

        res = []

        while (i < len(left) and j < len(right)):

            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        while i < len(left):
            res.append(left[i])
            i += 1

        while j < len(right):
            res.append(right[j])
            j += 1

        return res

    def mergeSort(self, nums):

        LEN = len(nums)

        if LEN <= 1:
            return nums

        midpoint = LEN // 2

        left = self.mergeSort(nums[:midpoint])
        right = self.mergeSort(nums[midpoint:])

        return self.merge(left, right)

    def binary_search(self, nums, target):

        i = 0
        j = len(nums) - 1

        while (i <= j):
            midpoint = (i + j) // 2

            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                j = midpoint - 1
            else:
                i = midpoint + 1

        return -1

    def fourSum(self, unsorted_nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        mList = []
        n = len(unsorted_nums)

        nums = self.mergeSort(unsorted_nums)

        # Using Binary Search

        for i in range(0, n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    diff = target - (nums[i] + nums[j] + nums[k])
                    index = self.binary_search(nums[k+1:], diff)
                    if index != -1:
                        mList.append(
                            [nums[i], nums[j], nums[k], nums[k + 1 + index]])

        # Using two pointer

        # for a in range(0, n-3):
        #     for b in range(a+1, n-2):
        #         i = b + 1               # next to b
        #         j = n - 1               # last

        #         while i < j:
        #             if (target - (nums[a] + nums[b]) > nums[i] + nums[j]):
        #                 i += 1
        #             elif (target - (nums[a] + nums[b]) < nums[i] + nums[j]):
        #                 j -= 1
        #             else:
        #                 mList.append([nums[a], nums[b], nums[i], nums[j]])
        #                 i += 1
        #                 j -= 1

        mList = [list(x) for x in set(tuple(x) for x in mList)]
        return mList


# @lc code=end
s = Solution()
s.fourSum([1, 0, -1, 0, -2, 2], 0)
s.fourSum([2, 2, 2, 2, 2], 8)
