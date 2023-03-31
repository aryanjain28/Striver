#
# @lc app=leetcode id=1268 lang=python
#
# [1268] Search Suggestions System
#

# @lc code=start
class Solution(object):

    def getMinMax(self, products, searchStr, type):

        searchLen = len(searchStr)
        i = 0
        j = len(products) - 1

        res = -1
        while i <= j:

            mid = (i + j) // 2
            subStr = products[mid][:searchLen]

            if subStr == searchStr:
                res = mid
                if type > 0:  # max
                    i = mid + 1
                else:  # min
                    j = mid - 1

            elif subStr < searchStr:
                i = mid + 1

            else:
                j = mid - 1

        return res

    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """

        products.sort()

        res = []
        for index in range(len(searchWord)):

            min_value = self.getMinMax(products, searchWord[:index + 1], -1)
            max_value = self.getMinMax(products, searchWord[:index + 1], 1) + 1

            res.append(products[
                min_value:
                min(min_value + 3, max_value)
            ])

        return res


# @lc code=end
