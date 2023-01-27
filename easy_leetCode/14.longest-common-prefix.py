#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    # def longestCommonPrefix(self, strs):

    # """
    # :type strs: List[str]
    # :rtype: str
    # """

    # if len(strs) > 1:
    #     first = strs[0]
    #     second = strs[1]

    #     res = []
    #     min = len(first) if len(first) < len(second) else len(second)
    #     i = 0

    #     while i < min:
    #         if first[i] == second[i]:
    #             res.append(first[i])
    #         else:
    #             break
    #         i += 1

    #     for string in strs[2:]:

    #         if len(string) < 1:
    #             return ""

    #         k = 0
    #         while (k < len(string) and k < len(res)):
    #             if (string[k] != res[k]):
    #                 break
    #             k += 1

    #         res = res[:k]

    #         if len(res) < 1:
    #             return ""

    #     return ''.join(res)

    # else:
    #     return strs[0]

    def common(self, left, right):
        res = ""
        i = 0
        while i < min(len(left), len(right)):
            if left[i] == right[i]:
                res += left[i]
            else:
                return res
            i += 1

        return res

    def split(self, strs):

        if len(strs) == 1:
            return strs[0]

        leftArr = self.split(strs[:len(strs) // 2])
        rightArr = self.split(strs[len(strs) // 2:])

        return self.common(leftArr, rightArr)

    # Divide and Conquer

    def longestCommonPrefix(self, strs):

        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        return self.split(strs)


# @lc code=end
s = Solution()

input_strs = ["flower", "flight"]
output = s.longestCommonPrefix(input_strs)
print(output)

input_strs = ["abab", "aba", ""]
output = s.longestCommonPrefix(input_strs)
print(output)

input_strs = ["baab", "bacb", "b", "cbc"]
output = s.longestCommonPrefix(input_strs)
print(output)

input_strs = ["leetcode", "leet", "lee", "le"]
output = s.longestCommonPrefix(input_strs)
print(output)

input_strs = ["a"]
output = s.longestCommonPrefix(input_strs)
print(output)
