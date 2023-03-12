#
# @lc app=leetcode id=838 lang=python
#
# [838] Push Dominoes
#

# @lc code=start

from collections import deque


class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """

        olderState = ""
        while dominoes != olderState:
            olderState = dominoes

            dominoes = dominoes.replace("R.L", "XXX")
            dominoes = dominoes.replace(".L", "LL")
            dominoes = dominoes.replace("R.", "RR")

        return dominoes.replace("XXX", "R.L")

        # 2nd Way

        # q = deque()
        # dominoes = list(dominoes)
        # [q.append((i, d)) for i, d in enumerate(dominoes) if d != "."]

        # while q:
        #     index, domino = q.popleft()
        #     if domino == "L" and index > 0 and dominoes[index - 1] == ".":
        #         dominoes[index - 1] = "L"
        #         q.append((index-1, "L"))
        #     elif domino == "R" and index < len(dominoes) - 1 and dominoes[index+1] == ".":
        #         if index < len(dominoes) - 2 and dominoes[index+2] == "L":
        #             q.popleft()
        #             pass
        #         else:
        #             dominoes[index + 1] = "R"
        #             q.append((index + 1, "R"))

        # return "".join(dominoes)


# @lc code=end
