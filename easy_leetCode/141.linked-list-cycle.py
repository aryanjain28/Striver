#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # Using fast and slow pointers
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False

        # Changing the value to NONE
        # curr = head
        # while curr:

        #     if curr.val == None:
        #         return True

        #     curr.val = None
        #     curr = curr.next

        # return False

        # Using Array
        # lasts = []

        # curr = head
        # while curr and curr.next:
        #     if curr.next in lasts:
        #         return True
        #     lasts.append(curr)
        #     curr = curr.next

        # return False


# @lc code=end
