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

        # print(products)

        res = []
        for i, _ in enumerate(searchWord):

            c = searchWord[:i+1]

            # res.append(
            #     [r for r in products[index: index + 3] if r.startswith(c)])

            index = self.getMinMax(products, c, -1)
            # max_value = self.getMinMax(products, searchWord[:index + 1], 1) + 1

            # print(c, index)

            res.append(
                [r for r in products[index: index + 3] if r.startswith(c)])

            # res.append(products[
            #     min_value:
            #     min(min_value + 3, max_value)
            # ])

        # print(res)
        return res


# @lc code=end

Solution().suggestedProducts(
    ["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse")
