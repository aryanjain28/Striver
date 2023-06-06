#
# @lc app=leetcode id=684 lang=python
#
# [684] Redundant Connection
#

# @lc code=start
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        parent = [-1] + [i for i in range(1, len(edges)+1)]

        def find(p):
            if p == parent[p]:
                return p
            return find(parent[p])            
        
        for (v1, v2) in edges:
            p1, p2 = find(v1), find(v2)
            if p1 == p2:
                return [v1, v2]

            parent[p2] = p1

 


# @lc code=end
print(Solution().findRedundantConnection([[1,2], [1,3], [2,3]]))
print(Solution().findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))
print(Solution().findRedundantConnection([[3,4],[1,2],[2,4],[3,5],[2,5]]))
print(Solution().findRedundantConnection([[1,5],[3,4],[3,5],[4,5],[2,4]]))