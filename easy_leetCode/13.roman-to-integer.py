#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        sum = 0

        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        for n in s:
            sum += {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
            }[n]
    
        # while i < len(s):
        #     j = i + 1
        #     curr = self.getInteger(s[i])
        #     if j < len(s):
        #         next = self.getInteger(s[j])
        #     else:
        #         next = 0
            
        #     if(curr < next): 
        #         sum += (next - curr)
        #         i += 1
        #     else: 
        #         sum += curr

        #     i += 1

        return sum 
            
        
# @lc code=end
s = Solution()
print(s.romanToInt("CCCIV"))
print(s.romanToInt("III"))
