#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
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

    def merge_sort(self, arr):

        LEN = len(arr)

        if LEN <= 1:
            return arr

        left = self.merge_sort(arr[:LEN // 2])
        right = self.merge_sort(arr[LEN // 2:])

        return self.merge(left, right)

    def binary_search(self, arr, target):

        LEN = len(arr)
        i = 0
        j = LEN - 1

        while i <= j:
            mid_point = (i + j) // 2

            if arr[mid_point] == target:
                return mid_point
            elif arr[mid_point] > target:
                j = mid_point - 1
            else:
                i = mid_point + 1

        return -1

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # nums = self.merge_sort(nums)
        # print(nums)
        # mList = []
        # mDict = {}
        # # for i, n in enumerate(nums[1:]):
        # i = 1
        # while i < len(nums):
        #     n = nums[i]
        #     if n in mDict and len(mDict[n]) < 3:
        #         mList.append(mDict[n]+[n])
        #         mDict[n] = mDict[n] + [n]
        #     elif n not in mDict:
        #         mDict[-(n + nums[i-1])] = [n, nums[i-1]]
        #     print(mDict)
        #     i += 1

        # print(mList)
        # print(mDict)
        # if nums[0] in mDict and len(mDict[nums[0]]) < 3:
        #     mList.append(mDict[nums[0]]+[nums[0]])

        # print(mList)
        # return mList

        # s_nums = self.merge_sort(nums)
        # LEN = len(nums)
        # i = 0
        # mList = []
        # mDict = {}
        # print(s_nums)
        # minimum = s_nums[0]
        # maximum = s_nums[-1]
        # breakAll = False

        # while i < LEN - 2:
        #     j = i + 1
        #     a = s_nums[i]

        #     if a > 0:
        #         break

        #     if breakAll:
        #         break

        #     while j < LEN - 1:
        #         b = s_nums[j]
        #         target = -(a+b)

        #         if target < a:
        #             breakAll = True

        #         if a > 0 and b > 0:
        #             break
        #         elif a == b:
        #             j += 1
        #             continue

        #         if target < minimum or target > maximum:
        #             j += 1
        #             continue

        #         elif (a, b) in mDict:
        #             j += 1
        #             continue

        #         elif target >= b:
        #             k = j + 1
        #             while k < LEN:
        #                 if s_nums[k] == target:
        #                     mList.append([s_nums[i], s_nums[j], s_nums[k]])
        #                     mDict[s_nums[i], s_nums[j]] = True
        #                     break
        #                 elif s_nums[k] > target:
        #                     break

        #                 k += 1
        #         j += 1
        #     i += 1

        # print(s_nums)

        # while i < LEN - 2:
        #     j = i + 1
        #     while j < LEN - 1:
        #         if ((s_nums[i], s_nums[j]) not in mDict or (s_nums[j], s_nums[i]) not in mDict):
        #             diff = -(s_nums[i] + s_nums[j])
        #             index = self.binary_search(s_nums[j+1:], diff)

        #             if index != -1:
        #                 mList.append(
        #                     [s_nums[i], s_nums[j], s_nums[j + 1 + index]])
        #                 mDict[s_nums[i], s_nums[j]] = j + 1 + index
        #                 mDict[s_nums[j], s_nums[i]] = j + 1 + index
        #             else:
        #                 mDict[s_nums[i], s_nums[j]] = -1
        #                 mDict[s_nums[j], s_nums[i]] = -1

        #     j += 1
        # i += 1

        mList = []
        mDict = {}
        s_nums = self.merge_sort(nums)
        i = 0
        j = 0
        LEN = len(nums)

        while i < LEN - 2:

            if s_nums[i] > 0:
                break

            j = i + 1
            k = LEN - 1
            while j < k:

                a = s_nums[i]
                b = s_nums[j]
                b_next = s_nums[j+1]
                c = s_nums[k]

                if -a < b + b_next:
                    break

                if b+c == -a and (a, b, c) not in mDict:
                    mList.append([a, b, c])
                    mDict[a, b, c] = True
                    j += 1
                    k -= 1
                elif b+c < -a:
                    j += 1
                else:
                    k -= 1

            i += 1
            while s_nums[i] == s_nums[i-1] and i < LEN - 2:
                i += 1

        # mList = [list(x) for x in set(tuple(x) for x in mList)]
        return mList


# @lc code=end
s = Solution()
# s.threeSum([-1, 0, 1])
# s.threeSum([3,-2,1,0])
# s.threeSum([-1, 0, 1, 0, 2, 2, 3, 4])
s.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 0, 4])
# s.threeSum([0, 0, 0, 0, 0, 0, 0, 0, 0])
