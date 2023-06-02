#
# @lc app=leetcode id=210 lang=python
#
# [210] Course Schedule II
#

# @lc code=start
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        mDict = {}
        visited = set()
        cycle = set()
        res = []

        mDict = {c: [] for c in range(numCourses) }
        for c, p in prerequisites:
            mDict[c].append(p)

        def dfs(course):

            if course in visited:
                return True
            
            if course in cycle:
                return False

            cycle.add(course)
            for preReq in mDict[course]:
                if not dfs(preReq):
                    return False
                
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
            
        return res


        
# @lc code=end
Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]])

