#
# @lc app=leetcode id=1461 lang=python
#
# [1461] Check If a String Contains All Binary Codes of Size K
#

# @lc code=start
class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        mSet = set()
        for i in range(len(s)-k+1):
            mSet.add(int(s[i:i+k], 2))

        return len(mSet) == 2**k


# @lc code=end
