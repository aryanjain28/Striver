#
# @lc app=leetcode id=1888 lang=python
#
# [1888] Minimum Number of Flips to Make the Binary String Alternating
#

# @lc code=start
class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Brute O(n^2)

        # LEN = len(s)

        # patt1 = ("01" * LEN) + ("0" if LEN % 2 == 1 else "")
        # patt2 = ("10" * LEN) + ("1" if LEN % 2 == 1 else "")

        # p1Count = 10**5
        # p2Count = 10**5

        # i = 0
        # while i < LEN:
        #     j = 0

        #     currP1Count = 0
        #     currP2Count = 0

        #     while j < LEN:

        #         if s[j] != patt1[j]:
        #             currP1Count += 1

        #         if s[j] != patt2[j]:
        #             currP2Count += 1

        #         j += 1
        #     s = s[1:] + s[0]

        #     p1Count = min(currP1Count, p1Count)
        #     p2Count = min(currP2Count, p2Count)

        #     i += 1

        # return min(p1Count, p2Count)

        # Optimized : O(n)
        LEN = len(s)

        patt1 = "01" * LEN
        patt2 = "10" * LEN

        patt1Count = 0
        patt2Count = 0

        i = 0
        while i < LEN:
            if patt1[i] != s[i]:
                patt1Count += 1

            if patt2[i] != s[i]:
                patt2Count += 1

            i += 1

        currPatt1Count = patt1Count
        currPatt2Count = patt2Count

        s += s[:LEN-1]

        print(s, patt1, patt2)

        i = LEN
        while i < len(s):

            # print(s[i], patt1[i], patt2[i])

            currPatt1Count -= 1
            currPatt2Count -= 1

            if s[i] != patt1[i]:
                currPatt1Count += 1

            if s[i] != patt2[i]:
                currPatt2Count += 1

            print(currPatt1Count, currPatt2Count)

            patt1Count = min(patt1Count, currPatt1Count)
            patt2Count = min(patt2Count, currPatt2Count)

            i += 1

        print(patt1Count, patt2Count)

        # LEN = len(s)
        # if len(set(s)) == 1:
        #     return LEN // 2

        # if LEN == 2:
        #     return 0

        # i = 0
        # while s[0] == s[1] and i < LEN:
        #     s = s[1:] + s[0]
        #     i += 1

        # count = 0
        # i = 2
        # while i <= LEN - 2:

        #     if s[i] != (s[0] + s[1])[0]:
        #         count += 1

        #     if s[i+1] != (s[0] + s[1])[1]:
        #         count += 1

        #     i += 2

        # return count


# @lc code=end
# print(Solution().minFlips("01001001101"))
# print(Solution().minFlips("101"))
print(Solution().minFlips("111000"))
