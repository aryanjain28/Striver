#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        mDict1 = {}
        mDict2 = {0: set()}
        for n in nums:
            mDict1[n] = 1 if n not in mDict1 else mDict1[n] + 1
            if mDict1[n] not in mDict2:
                mDict2[mDict1[n]] = {n}
            else:
                mDict2[mDict1[n]].add(n)

        result = {}
        j = len(nums)
        while j > 0 and len(result) < k:
            if j in mDict2:
                result = mDict2[j]
                if len(mDict2[j]) < len(mDict2[j-1]):
                    result = mDict2[j].intersection(mDict2[j-1])
            j -= 1
        return list(result)


# @lc code=end
