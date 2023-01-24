#
# @lc app=leetcode id=62 lang=python
#
# [62] Unique Paths
#

# @lc code=start
class Solution(object):
    def uniquePaths(self, m, n):
        M = m+n-2
        N = n-1

        res = 1
        for i in range(1, (M-N)+1):
            res = res * (i+N)/i

        return res


        
# @lc code=end

sol = Solution()
output = sol.uniquePaths(3, 7)
print(output)
