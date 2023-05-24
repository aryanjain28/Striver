#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#

# @lc code=start
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []

        def backtrack(comb, options, currSum):
            if currSum >= target:
                if currSum == target:
                    res.append(comb)
                return

            for index in range(len(options)):
                if index > 0 and options[index-1] == options[index]:
                    continue
                backtrack(comb+[options[index]], options[index+1:], currSum + options[index])
                if currSum + options[index] >= target:
                    break

            return res

        candidates.sort()
        return backtrack([], candidates, 0)


# @lc code=end
print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))
print(Solution().combinationSum2([2,5,2,1,2], 5))
print(Solution().combinationSum2([1,1,1,1,1,1,1,1], 5))

