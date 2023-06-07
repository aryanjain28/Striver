#
# @lc app=leetcode id=947 lang=python
#
# [947] Most Stones Removed with Same Row or Column
#

# @lc code=start
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """

        parent = {}

        def find(p):
            if p != parent[p]:
                parent[p] = find(parent[p])    
            return parent[p]

        def union(v1, v2):
            parent.setdefault(v1, v1)
            parent.setdefault(v2, v2)

            parent[find(v1)] = find(v2)

        for i, j in stones:
            union(i, ~j)

        return len(stones) - len({find(key) for key in parent })

        
# @lc code=end

Solution().removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])