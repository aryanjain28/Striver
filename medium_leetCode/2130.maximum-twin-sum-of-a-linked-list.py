#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        # Using reversing

        slow = fast = head
        last = None
        while fast and fast.next:

            fast = fast.next.next

            next = slow.next
            slow.next = last
            last = slow
            slow = next

        max_val = 0
        while slow and last:
            max_val = max(max_val, slow.val + last.val)
            slow = slow.next
            last = last.next

        return max_val

        # Using stack
        # mStack = []

        # dummy = ListNode(0, head)
        # slow = fast = dummy

        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        #     mStack.append(slow.val)

        # max_val = 0
        # curr = slow.next
        # while curr:
        #     max_val = max(max_val, mStack.pop() + curr.val)
        #     curr = curr.next

        # return max_val

# @lc code=end
