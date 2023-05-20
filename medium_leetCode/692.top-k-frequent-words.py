#
# @lc app=leetcode id=692 lang=python
#
# [692] Top K Frequent Words
#

from heapq import heappop, heapify
# @lc code=start


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        freq = {}
        for w in words:
            freq[w] = 1 if w not in freq else freq[w] + 1

        # heap = [(-val, key) for key, val in freq.items()]
        # heapify(heap)
        # return [heappop(heap)[1] for _ in range(k)]
    
        # using sorted function
        return sorted(freq, key=lambda p : (-freq[p], p))[:k]

# @lc code=end





Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
Solution().topKFrequent(["the", "day", "is", "sunny",
                         "the", "the", "the", "sunny", "is", "is"], 4)
