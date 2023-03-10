#
# @lc app=leetcode id=179 lang=python
#
# [179] Largest Number
#

# @lc code=start
from functools import cmp_to_key


class Solution(object):

    def largestNumber(self, nums):
        """
         :type nums: List[int]
         :rtype: str
         """
        cmp_func = lambda x,y: -1 if x+y > y+x else 0
        res = "".join(sorted(map(str, nums), key=cmp_to_key(cmp_func)))
        return "0" if res[0] == "0" else res


# @lc code=end
