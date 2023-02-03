#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#

# @lc code=start
class Solution(object):

    def merge(self, left, right):

        i = 0
        j = 0
        arr = []

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                arr.append(left[i])
                i += 1
            else:
                arr.append(right[j])
                j += 1

        while i < len(left):
            arr.append(left[i])
            i += 1

        while j < len(right):
            arr.append(right[j])
            j += 1

        return arr

    def merge_sort(self, arr):

        LEN = len(arr)
        if LEN <= 1:
            return arr

        left = self.merge_sort(arr[:LEN // 2])
        right = self.merge_sort(arr[LEN // 2:])

        return self.merge(left, right)

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # maxArea = -1
        # LEN = len(height)
        # sorted_height = self.merge_sort(height)
        # for i, H in enumerate(sorted_height):

        #     if i != 0 and i != LEN - 1:
        #         L = max(LEN - i - 1, i)
        #         area = L * H
        #         print(L, H, area)
        #         if maxArea < area:
        #             maxArea = area

        # Brute
        # i = 0
        # maxArea = -1
        # while i < len(height) - 1:
        #     j = i + 1
        #     while j < len(height):
        #         L = min(height[i], height[j])
        #         W = j - i
        #         area = L * W
        #         if area > maxArea:
        #             maxArea = area
        #         j += 1
        #     i += 1

        # Optimal O(n)

        maxArea = -1
        LEN = len(height)
        left_pointer = 0
        right_pointer = LEN - 1

        while left_pointer < right_pointer:
            area = (right_pointer - left_pointer) * \
                min(height[left_pointer], height[right_pointer])
            maxArea = max(area, maxArea)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            elif height[left_pointer] > height[right_pointer]:
                right_pointer -= 1
            else:
                left_pointer += 1
                right_pointer -= 1

        print(maxArea)
        return maxArea


# @lc code=end
s = Solution()
s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
