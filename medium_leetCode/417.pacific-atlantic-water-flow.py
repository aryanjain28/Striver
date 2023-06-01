#
# @lc app=leetcode id=417 lang=python
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        ROW_LEN, COL_LEN = len(heights), len(heights[0])

        pac = set()
        alt = set()

        def backtrack(r, c, h, visited):
            if r < 0 or\
                c < 0 or\
                r >= ROW_LEN or\
                c >= COL_LEN or\
                (r, c) in visited or\
                heights[r][c] < h:
                return
            
            visited.add((r, c))

            for (x,y) in [(-1,0), (1,0), (0,-1), (0,1)]:
                backtrack(r+x, c+y, heights[r][c], visited)
            
        for c in range(COL_LEN):
            backtrack(0, c, heights[0][c], pac)
            backtrack(ROW_LEN-1, c, heights[ROW_LEN-1][c], alt)    

        for r in range(ROW_LEN):
            backtrack(r, 0, heights[r][0], pac)
            backtrack(r, COL_LEN-1, heights[r][COL_LEN-1], alt)

        res = []
        for r in range(ROW_LEN):
            for c in range(COL_LEN):
                if (r, c) in pac and (r, c) in alt:
                    res.append([r, c])

        return res        
# @lc code=end
print(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
# print(Solution().pacificAtlantic([[4,2,3,2,1]]))
