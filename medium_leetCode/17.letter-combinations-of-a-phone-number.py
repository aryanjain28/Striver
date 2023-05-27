#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        res = []

        # using map
        mMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def bactrack(index, currS):
            if len(currS) == len(digits):
                res.append(currS)
                return

            for letter in mMap[digits[index]]:
                bactrack(index+1, currS + letter)

        bactrack(0, "")
        return res

# @lc code=end


print(Solution().letterCombinations(""))
