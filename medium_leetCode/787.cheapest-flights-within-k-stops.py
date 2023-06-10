#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#


from heapq import heappop, heappush
# @lc code=start
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """

        # using Dijkstra Algorithm

        adjList = {i: [] for i in range(n)}
        for s, d, p in flights:
            adjList[s].append((d, p))

        shortest = {}

        # Heap => storing (distance, node) => wrong approach!
        # pq = [(0, src)]

        # while pq:
        #     cost, node = heappop(pq)

        #     if node not in shortest:
        #         shortest[node] = cost
        #         for neighbor, price in adjList[node]:
        #             heappush(pq, (cost+price, neighbor))

        # print(shortest, shortest[dst])


        # Heap => (stops, dest, cost)
        pq = [(0, src, 0)]
        while pq:

            stops, node, cost = heappop(pq)

            if stops > k + 1:
                continue

            if node not in shortest or cost < shortest[node]:
                shortest[node] = cost

                if node != dst:
                    for neighbor, price in adjList[node]:
                        heappush(pq, (stops + 1,  neighbor, cost+price))

        if dst not in shortest:
            return -1
        return shortest[dst]


        # Using Bellman Ford algorithm
        # main = [float("inf")] * n
        # main[src] = 0

        # for _ in range(k+1):

        #     tmp = main.copy()

        #     for s, d, p in flights:

        #         if main[s] == float("inf"):
        #             continue

        #         if main[s] + p < tmp[d]:
        #             tmp[d] = main[s] + p

        #     main = tmp

        # return -1 if main[dst] == float("inf") else main[dst]
        
# @lc code=end
print(Solution().findCheapestPrice(3, [[0,1,100],[0,2,500],[1,2,100]], 0, 2, 1))
# print(Solution().findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))
