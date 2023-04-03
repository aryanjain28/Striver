#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # Using two pointers.
        dummy = ListNode()
        dummy.next = head

        slow = dummy
        fast = head

        while n > 0:
            fast = fast.next
            n -= 1

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

        # Using LEN (length) - O(n)
        # LEN = 0
        # curr = head
        # while curr:
        #     LEN += 1
        #     curr = curr.next

        # if LEN < 2:
        #     return None

        # LEN -= (n+1)
        # curr = head

        # if LEN >= 0:
        #     while LEN > 0:
        #         LEN -= 1
        #         curr = curr.next

        #     curr.next = curr.next.next
        #     return head

        # else:
        #     while LEN < 0:
        #         LEN += 1
        #         curr = curr.next

        #     return curr

# @lc code=end
