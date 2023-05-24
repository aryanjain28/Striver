#
# @lc app=leetcode id=47 lang=python
#
# [47] Permutations II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        LEN = len(nums)

        def backtrack(uPerm, options):

            if len(uPerm) == LEN:
                res.append(uPerm)
                return

            for index in range(len(options)):
                if index > 0 and options[index] == options[index-1]:
                    continue
                backtrack(uPerm + [options[index]], options[:index]+options[index+1:])
            
            return res

        nums.sort()
        return backtrack([], nums)

# @lc code=end


Solution().permuteUnique([1, 1, 2])
Solution().permuteUnique([1, 2, 3])
