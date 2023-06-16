#
# @lc app=leetcode id=740 lang=python
#
# [740] Delete and Earn
#

from collections import Counter
# @lc code=start
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        freq = Counter(nums)
        nums = sorted(list(set(nums)))

        r1 = 0
        r2 = nums[0] * freq[nums[0]]

        for i in range(1, len(nums)):
            num = nums[i] * freq[nums[i]]
            num += r2 if nums[i]-1 != nums[i-1] else r1

            r1 = r2
            r2 = max(num, r2)

        return r2



        
# @lc code=end

# Solution().deleteAndEarn([3,4,2])
# Solution().deleteAndEarn([2,2,3,3,3,4])
# Solution().deleteAndEarn([1,2,3])
# Solution().deleteAndEarn([8,3,4,7,6,6,9,2,5,8,2,4,9,5,9,1,5,7,1,4])
Solution().deleteAndEarn([1,1,1,2,4,5,5,5,6])