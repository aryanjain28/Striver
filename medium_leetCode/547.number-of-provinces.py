#
# @lc app=leetcode id=547 lang=python
#
# [547] Number of Provinces
#

# @lc code=start
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """




        # Using Union find
        n = len(isConnected)
        parent = [i for i in range(0, n)]

        def find(p):
            while p != parent[p]:
                p = parent[p]
            return p

        for i in range(0, n-1):
            for j in range(1, n):
                if isConnected[i][j] == 1:
                    p1, p2 = find(i), find(j)
                    parent[p2] = p1

        temp = set()
        for p in parent:
            temp.add(find(p))

        return len(temp)

        
# @lc code=end
Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
Solution().findCircleNum([[1,0,0],[0,1,0],[0,0,1]])
Solution().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])
