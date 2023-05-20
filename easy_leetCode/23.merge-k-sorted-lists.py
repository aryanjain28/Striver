#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists
#

from heapq import heapify, heappop, heappush

# @lc code=start
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        # LEN = len(lists)
        # if LEN == 0:
        #     return None

        # if LEN == 1:
        #     return lists[0]

        mainL = []
        for node in lists:
            while node:
                mainL.append(node.val)
                node = node.next

        if not mainL:
            return None

        mainL.sort()
        root = node = ListNode(mainL.pop(0))
        while mainL:
            node.next = ListNode(mainL.pop(0))
            node = node.next

        return root
    


        # using heap
        # heap = []
        # for node in lists:
        #     while node:
        #         heappush(heap, node.val)
        #         node = node.next

        # if not heap:
        #     return None
            
        # root = node = ListNode(heappop(heap))
        # while heap:
        #     node.next = ListNode(heappop(heap))
        #     node = node.next

        # return root


# @lc code=end

# Solution().mergeKLists([[1, 4, 5], [1, 3, 4], [2, 6]])
