#
# @lc app=leetcode id=1049 lang=python
#
# [1049] Last Stone Weight II
#

# @lc code=start
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        total = sum(stones)
        mStone = max(stones)
        if mStone >= total:
            return abs(2*mStone - total)

        capacity = total // 2

        r = [0] * (capacity+1)

        for stone in stones:
            for j in range(capacity, -1, -1):
                if j >= stone:
                    r[j] = (stone + r[j-stone]) if (stone + r[j-stone]) > (r[j]) else r[j]
                else:
                    break

        return abs(2 * r[-1] - total)


        
# @lc code=end
print(Solution().lastStoneWeightII([2,7,4,1,8,1]))
print(Solution().lastStoneWeightII([31,26,33,21,40]))
print(Solution().lastStoneWeightII([1,1,4,2,2]))
