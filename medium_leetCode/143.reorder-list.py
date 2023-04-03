#
# @lc app=leetcode id=143 lang=python
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        if head.next == None:
            return head

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None

        last = None

        # reversing - second portion
        while second:
            next = second.next
            second.next = last
            last = second
            second = next

        # merging
        first = head
        second = last

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next


# @lc code=end
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
# Solution().reorderList(head)
