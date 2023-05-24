#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []

        def backtrack(combination, options, currSum):

            if currSum >= target:
                if currSum == target:
                    res.append(combination)
                return

            for index, option in enumerate(options):
                backtrack(combination + [option], options[index:], currSum + option)
                if currSum + option >= target:
                    break

            return res

        candidates.sort()
        return backtrack([], candidates, 0)


# @lc code=end
print(Solution().combinationSum([2, 3, 6, 7], 7))
print(Solution().combinationSum([2, 3, 5], 8))
print(Solution().combinationSum([2], 1))

