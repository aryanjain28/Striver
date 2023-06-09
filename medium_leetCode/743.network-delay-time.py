#
# @lc app=leetcode id=743 lang=python
#
# [743] Network Delay Time
#

from heapq import heappop, heappush

# @lc code=start
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        adjList = {i:[] for i in range(1, n+1)}
        for src, dest, time in times:
            adjList[src].append((dest, time))

        shortest = {i: float("inf") for i in range(1, n+1) }
        shortest[k] = 0
        
        pq = [(0, k)]

        while pq:
            time, node = heappop(pq) 
            if time > shortest[node]:
                continue
            for child, t in adjList[node]:
                if t+time < shortest[child]:
                    shortest[child] = t+time
                    heappush(pq, (t+time, child))

        maxV = max(shortest.values())
        return maxV if maxV < float("inf") else -1

# @lc code=end
print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
print(Solution().networkDelayTime([[1,2,1]], 2, 1))
print(Solution().networkDelayTime([[1,2,1]], 2, 2))
