#
# @lc app=leetcode id=973 lang=python
#
# [973] K Closest Points to Origin
#

from heapq import heappop, heappush, nsmallest

# @lc code=start


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]
    
        # heap = []
        # for (x, y) in points:
        #     d = -(x**2 + y**2)
        #     heappush(heap, (d, (x, y)))
        #     if len(heap) > k:
        #         heappop(heap)

        # return [point for (_, point) in heap]



        # dis2Org = {}
        # distances = []
        # for point in points:
        #     d = (point[0]**2 + point[1]**2)
        #     distances.append(d)
        #     dis2Org[d] = dis2Org[d] + [point] if d in dis2Org else [point]

        # heapify(distances)
        # closest = []
        # while len(closest) < k:
        #     closest += dis2Org[heappop(distances)]
        # return closest


# @lc code=end

