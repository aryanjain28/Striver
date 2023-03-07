#
# @lc app=leetcode id=1963 lang=python
#
# [1963] Minimum Number of Swaps to Make the String Balanced
#

# @lc code=start
class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """

        # max_close = 0
        swaps = 0

        for c in s:
            if c == "[":
                swaps += 1
            elif swaps > 0:
                swaps -= 1
            # max_close = max(max_close, extraClose)

        return (swaps + 1) // 2

        # turn = 0
        # bal_L = 0
        # bal_R = 0
        # i = 0
        # j = len(s) - 1
        # while i < j:
        #     if s[i] == "]":
        #         if bal_L > -1:
        #             bal_L -= 1
        #     else:
        #         bal_L += 1

        #     if s[j] == "[":
        #         if bal_R > -1:
        #             bal_R -= 1
        #     else:
        #         bal_R += 1

        #     if bal_L >= 0:
        #         i += 1

        #     if bal_R >= 0:
        #         j -= 1

        #     if bal_L == -1 and bal_R == -1:
        #         turn += 1
        #         bal_L = 1
        #         bal_R = 1
        #         i += 1
        #         j -= 1

        # return turn


# @lc code=end
