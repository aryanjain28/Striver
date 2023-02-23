#
# @lc app=leetcode id=500 lang=python
#
# [500] Keyboard Row
#

# @lc code=start
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        res = []
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for word in words:
            for row in rows[::-1]:
                if set(row.lower()) >= (set(word.lower())):
                    res.append(word)
                    break

        return res


# @lc code=end
print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))
