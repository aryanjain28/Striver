#
# @lc app=leetcode id=203 lang=python
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        dummy = ListNode(0, head)
        curr = dummy
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next


# @lc code=end
head = ListNode(7, ListNode(7, ListNode(7, ListNode(7, None))))
# head = ListNode(1, ListNode(2, ListNode(6, ListNode(
#     3, ListNode(4, ListNode(5, ListNode(6, None)))))))
Solution().removeElements(head, 7)
