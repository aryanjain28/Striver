#
# @lc app=leetcode id=63 lang=python
#
# [63] Unique Paths II
#

# @lc code=start
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        # r = len(obstacleGrid)
        # c = len(obstacleGrid[0])
        
        # # recursion + topdown dp
        # cache = {}
        # def count(row, col):

        #     if row >= r or col >= c or obstacleGrid[row][col] == 1:
        #         return 0
            
        #     if (row, col) in cache:
        #         return cache[(row, col)]
            
        #     if row == r - 1 and col == c - 1:
        #         return 1

        #     cache[(row, col)] = count(row + 1, col) + count(row, col + 1)
        #     return cache[(row, col)]

        # return count(0, 0)

        n = len(obstacleGrid)       # rows
        m = len(obstacleGrid[0])    # cols


        # if n == 1 and m == 1:
        #     return 1 - (obstacleGrid[0][0])

        # if n == 1:
        #     return 0 if sum(set(obstacleGrid[0])) > 0 else 1
            
        # if m == 1:
        #     return 0 if sum(set([p[0] for p in obstacleGrid])) > 0 else 1
            
        if obstacleGrid[-1][-1] or obstacleGrid[0][0]:
            return 0

        r1 = [0] * m
        if obstacleGrid[-1][-1] != 1:
            r1[-1] = 1

        for curr in range(n-1, -1, -1):

            r2 = ([1] * (m-1)) + [r1[-1]]
                
            for index in range(m-1, -1, -1):
                if obstacleGrid[curr][index] == 1:
                    r2[index] = 0
                    continue

                r2[index] = r1[index] + (r2[index+1] if index < m-1 else 0)

            r1 = r2

        return r2[0]






        
# @lc code=end
Solution().uniquePathsWithObstacles([
    [0,0,0],
    [0,1,0],
    [0,0,0],
])

Solution().uniquePathsWithObstacles([
    [0,1],
    [1,0],
])

Solution().uniquePathsWithObstacles([
    [0,1],
    [0,0],
])

Solution().uniquePathsWithObstacles([
    [0,0],
    [0,1],
])

# Solution().uniquePathsWithObstacles([
#     [0,0],
#     [1,1],
#     [0,0],
# ])

# print(Solution().uniquePathsWithObstacles([
#     [0,0,1,0,0,0]
# ]))

# print(Solution().uniquePathsWithObstacles([
#     [1,1]
# ]))

# print(Solution().uniquePathsWithObstacles([
#     [0,0,1,0,0,0]
# ]))

# print(Solution().uniquePathsWithObstacles([
#     [0],[0]
# ]))

# print(Solution().uniquePathsWithObstacles([
#     [1],[0]
# ]))


# Solution().uniquePathsWithObstacles([
#     [0,0,0,0,0,0]
# ])

