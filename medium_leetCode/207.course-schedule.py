#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#

# @lc code=start
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        mDict = {}
        visited = set()

        for course, prereq in prerequisites:
            if course not in mDict:
                mDict[course] = []
            mDict[course].append(prereq)
                

        def backtrack(course):

            if course in visited:
                return False

            elif course not in mDict:
                return True
            
            visited.add(course)

            for c in mDict[course]:
                if not backtrack(c):
                    return False
                
            visited.remove(course)
            mDict[course] = []
            return True


        for course in range(numCourses):
            if not backtrack(course):
                return False
        
        return True
        


        
# @lc code=end
# print(Solution().canFinish(2, [[1,0]]))
# print(Solution().canFinish(2, [[1,0],[0,1]]))
print(Solution().canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))
# print(Solution().canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
