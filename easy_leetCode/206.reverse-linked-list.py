#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        curr = head
        last = None
        while curr:

            next = curr.next
            curr.next = last
            last = curr
            curr = next

        return last

        # curr = last
        # while curr:
        #     print(curr.val)
        #     curr = curr.next


# @lc code=end
