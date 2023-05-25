#
# @lc app=leetcode id=216 lang=python
#
# [216] Combination Sum III
#

# @lc code=start
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        res = []

        def backtrack(nums, options, currSum):
            if currSum >= n:
                if currSum == n and len(nums) == k:
                    res.append(nums)
                return
            for i, option in enumerate(options):
                if len(nums) + 1 > k or currSum + option > n:
                    break
                backtrack(nums + [option], options[i+1:], currSum + option)
        backtrack([], list(range(1, 10)), 0)
        return res

# @lc code=end


# print(Solution().combinationSum3(4, 1))
# print(Solution().combinationSum3(3, 9))
# print(Solution().combinationSum3(3, 7))
print(Solution().combinationSum3(9, 45))
