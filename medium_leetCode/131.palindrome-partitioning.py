#
# @lc app=leetcode id=131 lang=python
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        # Using backtracking

        res = []
        if not s:
            return res

        def backtrack(s, curr):

            if not s:
                res.append(curr)
                return

            for i in range(1, len(s)+1):

                if (s[:i])[::-1] == s[:i]:
                    backtrack(s[i:], curr+[s[:i]])

        backtrack(s, [])
        return res

        # def checkPalidrome(arr):
        #     for p in arr:
        #         if p[::-1] != p:
        #             return False
        #     return True

        # res = []

        # def backtrack(sArr):
        #     # print(res)
        #     # print(sArr)
        #     if len(sArr) == 1:
        #         return
        #     if checkPalidrome(sArr):
        #         # print("Checking: ", sArr)
        #         res.append(sArr)

        #     # print(checkPalidrome(sArr), sArr)

        #     for i in range(len(sArr)):
        #         if len(sArr) == 1 or i+1 == len(sArr):
        #             break
        #         backtrack(sArr[:i] + [sArr[i] + sArr[i+1]] + sArr[i+2:])

        # if checkPalidrome([s]):
        #     res.append([s])

        # backtrack(list(s))
        # return [list(x) for x in set(tuple(x) for x in res)]


# @lc code=end
# print(Solution().partition("aabb"))
# print(Solution().partition("aab"))
# print(Solution().partition("aa"))
# print(Solution().partition("a"))
print(Solution().partition("efe"))
