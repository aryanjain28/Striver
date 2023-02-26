#
# @lc app=leetcode id=978 lang=python
#
# [978] Longest Turbulent Subarray
#

# @lc code=start
class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        maxSize = 1
        currSize = 1
        last = 0

        for i, currN in enumerate(arr[1:]):
            i += 1
            lastN = arr[i - 1]

            if last == 0:
                if currN - lastN > 0:
                    last = 1
                    currSize += 1
                elif currN - lastN < 0:
                    last = -1
                    currSize += 1
            elif last == -1:
                if currN - lastN > 0:
                    last = 1
                    currSize += 1
                elif currN - lastN < 0:
                    last = -1
                    currSize = 2
                else:
                    last = 0
                    currSize = 1
            elif last == 1:
                if currN - lastN < 0:
                    last = -1
                    currSize += 1
                elif currN - lastN > 0:
                    last = 1
                    currSize = 2
                else:
                    last = 0
                    currSize = 1

            if currSize > maxSize:
                maxSize = currSize

        print(maxSize)
        return maxSize


# @lc code=end
Solution().maxTurbulenceSize([4, 8, 12, 16])
Solution().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9])
