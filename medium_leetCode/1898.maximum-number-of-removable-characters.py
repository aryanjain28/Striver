#
# @lc app=leetcode id=1898 lang=python
#
# [1898] Maximum Number of Removable Characters
#

# @lc code=start
class Solution(object):

    def maximumRemovals(self, s, p, removable):
        """
        :type s: str
        :type p: str
        :type removable: List[int]
        :rtype: int
        """

        def isSubSeq(s, p):
            i = 0
            for index, c in enumerate(s):
                if index in removed:
                    continue

                if c == p[i]:
                    i += 1
                    if i >= len(p):
                        return True
            return False

        res = 0

        i = 0
        j = len(removable) - 1
        while i <= j:

            nRemove = (i + j) // 2
            removed = set(removable[:nRemove + 1])

            # s_temp = s
            # for i in range(nRemove):
            #     s_temp = s_temp[:removable[i]] + \
            #         "0" + s_temp[removable[i] + 1:]

            # True
            if isSubSeq(s, p):
                i = nRemove + 1
                res = max(nRemove + 1, res)
            else:
                j = nRemove - 1

        return res


# @lc code=end
# print(Solution().maximumRemovals("abcacb", "ab", [3, 1, 0]))
# print(Solution().maximumRemovals("abcbddddd", "abcd", [3, 2, 1, 4, 5, 6]))
# print(Solution().maximumRemovals("abcab", "abc", [0, 1, 2, 3, 4]))
# print(Solution().maximumRemovals("qlevcvgzfpryiqlwy", "qlecfqlw", [12, 5]))
