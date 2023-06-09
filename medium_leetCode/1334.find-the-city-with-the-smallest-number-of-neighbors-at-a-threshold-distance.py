#
# @lc app=leetcode id=1334 lang=python
#
# [1334] Find the City With the Smallest Number of Neighbors at a Threshold Distance
#

from heapq import heappop, heappush

# @lc code=start
class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """

        adjList = {i: [] for i in range(n)}
        
        for src, dest, dist in edges:
            adjList[src].append((dest, dist))
            adjList[dest].append((src, dist))
            
        length, s, c = float("inf"), -1, -1
        for k in range(n):
            pq = [(0, k)]
            shortest = {}

            while pq:
                distance, city = heappop(pq)
                if distance > distanceThreshold:
                    break
                if city in shortest:
                    continue

                shortest[city] = distance
                for neighbor, d in adjList[city]:
                    if neighbor not in shortest:
                        heappush(pq, (d+distance, neighbor))

            if len(shortest) <= length:
                length = len(shortest)
                if sum(shortest.values()) > s:
                    c = k

        return c                

                



        
# @lc code=end
Solution().findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4)
Solution().findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2)
