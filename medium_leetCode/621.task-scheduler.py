#
# @lc app=leetcode id=621 lang=python
#
# [621] Task Scheduler
#

from heapq import heapify, heappop, heappush, heapreplace
from collections import Counter

# @lc code=start


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord("A")] += 1
        max_freq = max(freq)
        last_row = freq.count(max_freq)
        return max(len(tasks), ((max_freq - 1) * (n + 1) + last_row))    
    
# @lc code=end

        # using heap
        # heap = [0] * 26
        # for task in tasks:
        #     heap[ord(task) - 65] -= 1

        # heap = list(filter(lambda n: n != 0, heap))
        # heapify(heap)

        # q = []
        # time = 0
        # while heap or q:
        #     if q and q[0][1] == time:
        #         heappush(heap, q.pop(0)[0])

        #     if heap:
        #         f = heappop(heap) + 1
        #         if f != 0:
        #             q.append((f, n + time + 1))

        #     time += 1
        # return time



Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 0)
Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2)

Solution().leastInterval(
    ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)
# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
## RC ##
## APPROACH : HASHMAP ##
## LOGIC : TAKE THE MAXIMUM FREQUENCY ELEMENT AND MAKE THOSE MANY NUMBER OF SLOTS ##
# Slot size = (n+1) if n= 2 => slotsize = 3
# Example:
# {A:5, B:1}
# => ABxAxxAxxAxxAxx => indices of A = 0,2 and middle there should be n elements, so slot size should be n+1

# Ex: {A:6,B:4,C:2} n = 2
# final o/p will be
# slot size / cycle size = 3
# Number of rows = number of A's (most freq element)
# [
#     [A, B,      C],
#     [A, B,      C],
#     [A, B,      idle],
#     [A, B,      idle],
#     [A, idle,   idle],
#     [A   -        - ],
# ]
#
# so from above total time intervals = (max_freq_element - 1) * (n + 1) + (all elements with max freq)
# ans   =     rows_except_last   * columns +        last_row

# but consider {A:5, B:1, C:1, D:1, E:1, F:1, G:1, H:1, I:1, J:1, K:1, L:1} n = 1
# total time intervals by above formula will be 4 * 2 + 1 = 9, which is less than number of elements, which is not possible. so we have to return max(ans, number of tasks)

## TIME COMPLEXITY : O(N) ##
## SPACE COMPLEXITY : O(1) ##

# freq = collections.Counter(tasks)
# max_freq = max(freq.values())
# freq = list(freq.values())
# max_freq_ele_count = 0                 # total_elements_with_max_freq, last row elements
# i = 0
# while( i < len(freq)):
#     if freq[i] == max_freq:
#         max_freq_ele_count += 1
#     i += 1

# ans = (max_freq - 1) * (n+1) + max_freq_ele_count

# return max(ans, len(tasks))
