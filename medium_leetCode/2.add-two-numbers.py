#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = ListNode()
        curr = head
        extra = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum_val = (val1 + val2 + extra)
            extra = sum_val // 10

            # create node -> sum_Val
            curr.next = ListNode(sum_val % 10, None)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if extra > 0:
            curr.next = ListNode(1, None)

        return head.next


# @lc code=end
