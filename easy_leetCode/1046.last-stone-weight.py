#
# @lc app=leetcode id=1046 lang=python
#
# [1046] Last Stone Weight
#

# @lc code=start

from heapq import heappop, heappush, heapify, _heapify_max


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        while len(stones) > 1:
            stones.sort()
            diff = stones.pop() - stones.pop()
            if diff != 0:
                stones.append(diff)
        
        stones.append(0)
        return stones[0]


        # stones = [n*-1 for n in stones]
        # heapify(stones)
        # while len(stones) > 1:
        #     diff = heappop(stones) - heappop(stones)
        #     if diff != 0:
        #         heappush(stones, diff)
        # stones.append(0)
        # return -stones[0]
    
# @lc code=end
