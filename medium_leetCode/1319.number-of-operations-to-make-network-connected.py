#
# @lc app=leetcode id=1319 lang=python
#
# [1319] Number of Operations to Make Network Connected
#

# @lc code=start
class Solution(object):
    def makeConnected(self, n, connections):

        if len(connections) < n - 1:
            return -1

        wires = len(connections)                
        parent = list(range(n))
        size = [1] * n

        def find(p):
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(v1, v2):
            p1, p2 = find(v1), find(v2)
            if p1 != p2:
                if size[p1] < size[p2]:
                    parent[p1] = p2
                    size[p2] += size[p1]
                else:
                    parent[p2] = p1
                    size[p1] += size[p2]

        for (c1, c2) in connections:
            if find(c1) != find(c2):
                union(c1, c2)
                wires -= 1

        return len({find(p) for p in parent}) - 1


        
# @lc code=end
# print(Solution().makeConnected(4, [[0,1],[0,2],[1,2]]))
# print(Solution().makeConnected(6, [[0,1],[0,2],[0,3],[1,2],[1,3]]))
# print(Solution().makeConnected(5, [[0,1],[0,2],[3,4],[2,3]]))
print(Solution().makeConnected(12, [[1,5],[1,7],[1,2],[1,4],[3,7],[4,7],[3,5],[0,6],[0,1],[0,4],[2,6],[0,3],[0,2]]))



