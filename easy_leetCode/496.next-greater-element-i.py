#
# @lc app=leetcode id=496 lang=python
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        ans = nums1
        mDict = {}
        stack = []
        for i, n in enumerate(nums1):
            mDict[n] = i

        for n in nums2:
            while len(stack) > 0 and n > stack[-1]:
                ans[mDict[stack.pop()]] = n
            if n in mDict and (len(stack) == 0 or stack[-1] > n):
                stack.append(n)

        while len(stack) > 0:
            ans[mDict[stack.pop()]] = -1
        return ans

# @lc code=end
