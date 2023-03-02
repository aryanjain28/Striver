#
# @lc app=leetcode id=560 lang=python
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution(object):
    def subarraySum(self, nums, k):
        answer = 0
        mDict = {0: 1}
        i = 0
        while i < len(nums):
            nums[i] = nums[i] + (0 if i == 0 else nums[i-1])
            if nums[i] - k in mDict:
                answer += mDict[nums[i] - k]
            mDict[nums[i]] = 1 if nums[i] not in mDict else mDict[nums[i]] + 1
            i += 1
        return answer


# @lc code=end
