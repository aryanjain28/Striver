#
# @lc app=leetcode id=735 lang=python
#
# [735] Asteroid Collision
#

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids):

        res = []
        for _ in range(len(asteroids) - 1):
            d1 = asteroids.pop()
            d2 = asteroids.pop()

            if d1 < 0 and d2 < 0:
                return
            elif d1 > 0 and d2 > 0:
                return

            if abs(d1) > abs(d2):
                asteroids.append(d1)
            elif abs(d1) < abs(d2):
                asteroids.append(d2)

        return asteroids

# @lc code=end
