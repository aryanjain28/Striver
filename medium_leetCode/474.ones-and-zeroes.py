#
# @lc app=leetcode id=474 lang=python
#
# [474] Ones and Zeroes
#

from collections import Counter
# @lc code=start


class Solution(object):
    def findMaxForm(self, strs, M, N):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        strs = [(s.count("1"), s.count("0")) for s in strs]
        T = [[0]*(N+1) for _ in range(M+1)]

        for (oneCount, zeroCount) in strs:
            for m in range(M, zeroCount - 1, -1):
                for n in range(N, oneCount - 1, -1):
                    include = 1+T[m-zeroCount][n-oneCount]
                    if include > T[m][n]:
                        T[m][n] = include

        return T[-1][-1]


# @lc code=end
print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
# print(Solution().findMaxForm(["10", "0", "1"], 1, 1))
# print(Solution().findMaxForm(["00", "000"], 1, 10))
