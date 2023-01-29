#
# @lc app=leetcode id=12 lang=python
#
# [12] Integer to Roman
#

# @lc code=start
class Solution(object):

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        one_to_nine = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
        }

        roman = ""
        places = 1
        i = len(str(num)) - 1
        while (i >= 0):
            n = str(num)[i]
            if n != "0":
                curr_roman = one_to_nine[int(n)]
                if places == 10:
                    curr_roman = curr_roman.replace("X", "C").replace("I", "X").replace("V", "L")
                elif places == 100:
                    curr_roman = curr_roman.replace("X", "M").replace("I", "C").replace("V", "D")
                elif places == 1000:
                    curr_roman = curr_roman.replace("I", "M")

                roman = curr_roman + roman

            places *= 10
            i -= 1

        return roman


# @lc code=end
s = Solution()
print(s.intToRoman(1994))
