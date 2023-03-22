#
# @lc app=leetcode id=150 lang=python
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        mStack = []
        for i in range(len(tokens)):
            if tokens[i] not in "*/+-":
                mStack.append(int(tokens[i]))
            elif tokens[i] == "+":
                mStack.append(mStack.pop() + mStack.pop())
            elif tokens[i] == "-":
                mStack.append(-(mStack.pop() - mStack.pop()))
            elif tokens[i] == "*":
                mStack.append(mStack.pop() * mStack.pop())
            else:
                d1 = mStack.pop()
                d2 = mStack.pop()
                mStack.append(int(float(d2 / d1)))

        return mStack.pop()


# @lc code=end
Solution().evalRPN(["10", "6", "9", "3", "+",
                    "-11", "*", "/", "*", "17", "+", "5", "+"])
