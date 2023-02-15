#
# @lc app=leetcode id=67 lang=python
#
# [67] Add Binary
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        mDict = {
            "000": "0",
            "001": "1",
            "010": "1",
            "011": "0",
            "100": "1",
            "101": "0",
            "110": "0",
            "111": "1",
        }

        res = ""
        diff = "0"
        A_LEN = len(a)
        B_LEN = len(b)
        if A_LEN > B_LEN:
            b = "0" * (A_LEN - B_LEN) + b
        elif B_LEN > A_LEN:
            a = "0" * (B_LEN - A_LEN) + a

        i = len(a) - 1
        while i >= 0:
            res = mDict[diff + a[i] + b[i]] + res
            if a[i] == b[i] == "1" or b[i] == diff == "1" or a[i] == diff == "1":
                diff = "1"
            else:
                diff = "0"

            # if a[i] == b[i]:
            #     if a[i] == "0":
            #         if diff == "0":
            #             res = "0" + res
            #         else:
            #             res = "1" + res
            #             diff = "1"
            #     else:
            #         diff = "1"
            #         res = "0" + res
            # else:
            #     if diff == "1":
            #         res = "0" + res
            #         diff = "1"
            #     else:
            #         res = "1" + res
            #         diff = "0"

            i -= 1

        if diff == "1":
            return diff + res
        return res


# @lc code=end
# print(Solution().addBinary("1111", "1111"))
# print(Solution().addBinary("1", "111"))
print(Solution().addBinary("11", "1"))
