#
# @lc app=leetcode id=881 lang=python
#
# [881] Boats to Save People
#

# @lc code=start
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """

        people.sort(reverse=True)
        count = 0
        maxIndex = 0
        minIndex = len(people) - 1
        while maxIndex <= minIndex:
            if people[maxIndex] + people[minIndex] <= limit:
                minIndex -= 1
            maxIndex += 1
            count += 1

        return count


# @lc code=end
