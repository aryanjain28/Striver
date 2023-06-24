#
# @lc app=leetcode id=983 lang=python
#
# [983] Minimum Cost For Tickets
#

# @lc code=start
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """

        # capacity = 365
        # weights = [1, 7, 30]

        # M = len(costs)
        # N = capacity

        # T = [[0] * (capacity + 1) for _ in range(M+1)]
        # T[0][0] = 1

        # for i in range(1, M+1):
        #     T[i][0] = 1
        #     for cap in range(1, N+1):
        #         included = costs[i-1] + T[i-1][cap-weights[i-1]] if cap >= weights[i-1] else 0
        #         T[i][cap] = min(T[i-1][cap], included)

        # print(T)


        # LEN = len(days)
        # maxDay = days[-1]
        # def getIndex(index, day):
        #     if day > maxDay:
        #         return LEN
            
        #     for i in range(index+1,LEN):
        #         if days[i] >= day:
        #             return i
                
        # cache = {}
        # def rec(index, currCost):

        #     if index >= LEN or days[index] > maxDay:
        #         return currCost
            
        #     if (index, currCost) in cache:
        #         return cache[(index, currCost)]
            
        #     oneDay = rec(index+1, currCost + costs[0])
        #     sevenDay = currCost + costs[1] if days[index]+7 > maxDay else rec(getIndex(index, days[index]+7), currCost + costs[1])
        #     thirtyDay = currCost + costs[2] if days[index]+30 > maxDay else rec(getIndex(index, days[index]+30), currCost + costs[2])

        #     # oneDay = rec(index+1, currCost + costs[0])
        #     # sevenDay = currCost + costs[1] if days[index]+7 > maxDay else rec(getIndex(index, days[index]+7), currCost + costs[1])
        #     # thirtyDay = currCost + costs[2] if days[index]+30 > maxDay else rec(getIndex(index, days[index]+30), currCost + costs[2])
            
        #     cache[(index, currCost)] = min(oneDay, sevenDay, thirtyDay)
        #     return cache[(index, currCost)]
        
        # return rec(0,0)


        # T = [0] * (len(days))

        # for i in range(0, len(days)):

        #     i7, i30 = i, i

        #     while i7 > 0 and days[i7] > (days[i] - 7) > 0: i7 -= 1
        #     while i30 > 0 and days[i30] > (days[i] - 30) > 0: i30 -= 1

        #     T[i] = min(costs[0] + T[i-1], costs[1] + T[i7], costs[2] + T[i30])

        # return T[-1]

        LEN = len(days)
        T = [0] * (LEN+1)

        for i in range(LEN-1, -1, -1):

            i7, i30 = i, i

            while i7 < LEN and days[i7] < (days[i] + 7): i7 += 1
            while i30 < LEN and days[i30] < (days[i] + 30): i30 += 1

            T[i] = min(costs[0] + T[i+1], costs[1] + T[i7], costs[2] + T[i30])

        return T[0]

            










        
# @lc code=end
Solution().mincostTickets([1,4,6,7,8,20], [2,7,15])
Solution().mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15])
Solution().mincostTickets([1,2,3,4,6,8,9,10,13,14,16,17,19,21,24,26,27,28,29], [3, 14, 50] )

