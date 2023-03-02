#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mDict = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str not in mDict:
                mDict[sorted_str] = [str]
                continue
            mDict[sorted_str].append(str)
        return list(mDict.values())

# @lc code=end
