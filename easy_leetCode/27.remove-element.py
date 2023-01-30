#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        LEN = len(nums)

        if LEN == 0:
            return 0

        if LEN == 1:
            if nums[0] == val:
                return 0
            return 1

        i = 0
        j = i + 1

        while j < LEN:

            if nums[j] == val and nums[i] != val:
                i = j

            if nums[j] != val and nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                while i < j and nums[i] != val:
                    i += 1

            j += 1

        if i == 0 and nums[0] != val:
            return j
        return i


# @lc code=end
s = Solution()

output = s.removeElement([3, 2, 2, 3], 3)
print(output)

output = s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
print(output)

output = s.removeElement([2], 3)
print(output)

output = s.removeElement([2, 2, 2, 2, 2, 2, 2, 2], 3)
print(output)

output = s.removeElement([3, 3], 3)
print(output)
