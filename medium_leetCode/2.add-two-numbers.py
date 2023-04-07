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
        curr1 = l1
        curr2 = l2

        while curr1 or curr2:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            sum_val = (val1 + val2 + extra)
            extra = 1 if sum_val >= 10 else 0

            # create node -> sum_Val
            curr.next = ListNode(sum_val % 10, None)
            curr = curr.next

            curr1 = curr1.next if curr1 else curr1
            curr2 = curr2.next if curr2 else curr2

        if extra > 0:
            curr.next = ListNode(1, None)

        return head.next


# @lc code=end
