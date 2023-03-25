#
# @lc app=leetcode id=853 lang=python
#
# [853] Car Fleet
#

# @lc code=start
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        position.reverse()
        speed.reverse()

        count = 0
        while True:

            currPos = position.pop()
            currSpeed = speed.pop()

            if len(target) == 0:
                count += 1
                break

            if position[-1] == currPos:
                pass

            elif currPos + currSpeed <= position[-1] + speed[-1] <= target:
                
                position.append(max(currPos + currSpeed,  ))
                speed.append(min(currSpeed, speed.pop()))
                
                pass

        return count

# @lc code=end
