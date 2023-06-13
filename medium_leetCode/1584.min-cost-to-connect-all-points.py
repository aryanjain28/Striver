#
# @lc app=leetcode id=1584 lang=python
#
# [1584] Min Cost to Connect All Points
#

from heapq import heappop, heappush
# @lc code=start
class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        def distance(p1i, p2i):
            return abs(points[p1i][0] - points[p2i][0]) + abs(points[p1i][1] - points[p2i][1])


        n = len(points)
        visited = set()
        visited.add(0)

        mst = 0
        minHeap = [] # (wt, src, dest)
        for i in range(1, n):
            heappush(minHeap, (distance(0, i), 0, i))

        count = 0
        while count < n-1:
            _, src, dest = heappop(minHeap)

            if dest in visited or src == dest:
                continue

            visited.add(dest)
            mst += distance(src, dest)

            for nPoint in range(n):
                if nPoint not in visited and nPoint != dest:
                    heappush(minHeap, (distance(dest, nPoint), dest, nPoint))
            
            count += 1

        return mst

# @lc code=end
Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])
