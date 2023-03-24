#
# @lc app=leetcode id=739 lang=python
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures):
        mStack = [0]
        output = [0] * len(temperatures)
        index = 1
        while index < len(temperatures):
            while mStack and temperatures[mStack[-1]] < temperatures[index]:
                output[mStack.pop()] = index - mStack[-1]

            mStack.append(index)
            index += 1

        return output


# @lc code=end
