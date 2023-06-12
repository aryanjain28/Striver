#
# @lc app=leetcode id=1489 lang=python3
#
# [1489] Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
#

from heapq import heappop, heappush
# @lc code=start
class Solution(object):
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """

        def minimumSpanningTree(edgeIndex, weight):

            # edges => (src, dest, wt)
            adj = {i: [] for i in range(n)}
            for index, (src, dest, wt) in enumerate(edges):
                adj[src].append((dest, index, weight if index == edgeIndex else wt))
                adj[dest].append((src, index, weight if index == edgeIndex else wt))
            
            visited = set()
            visited.add(0)
            minHeap = []
            for (d, eIndex, w) in adj[0]:
                heappush(minHeap, (w, 0, d, eIndex))

            mst = 0
            while minHeap:

                wt, src, dest, eIndex = heappop(minHeap)

                if dest in visited or src == dest:
                    continue

                mst += wt
                visited.add(dest)

                for neighbor, eI, wt in adj[dest]:
                    if neighbor not in visited:
                        heappush(minHeap, (wt, dest, neighbor, eI))

            return mst + (edges[edgeIndex][-1] if weight == 0 else 0)
        

        minimumMst = minimumSpanningTree(0, edges[0][-1])
        

        p_critical, critical = [], []
        for edgeIndex in range(len(edges)): # len(edges) """
            mstScore = minimumSpanningTree(edgeIndex, float("inf")) # remove this edge
            if mstScore > minimumMst:
                critical.append(edgeIndex)

            mstScore = minimumSpanningTree(edgeIndex, 0) # must have this edge
            if mstScore == minimumMst:
                p_critical.append(edgeIndex)


        return [critical, list(set(p_critical) - set(critical))]





        
# @lc code=end
Solution().findCriticalAndPseudoCriticalEdges(5, [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]])
Solution().findCriticalAndPseudoCriticalEdges(4, [[0,1,1],[1,2,1],[2,3,1],[0,3,1]])
# Solution().findCriticalAndPseudoCriticalEdges(4, [[0,1,1],[1,2,1],[2,3,1],[0,3,1]])
