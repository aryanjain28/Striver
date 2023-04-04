#
# @lc app=leetcode id=234 lang=python
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # Using Stack
        mStack = []
        dummy = ListNode(0, head)
        slow = fast = dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            mStack.append(slow.val)

        slow = slow.next

        # Odd
        if fast == None:
            mStack.pop()

        while slow:
            if slow.val != mStack.pop():
                return False
            slow = slow.next

        return True

        # another WAY: reversing completely and checking
        # reversing
        # reverse = None
        # curr = head
        # while curr:
        #     reverse = ListNode(curr.val, reverse)
        #     curr = curr.next

        # # checking
        # curr = head
        # while curr and reverse:
        #     if curr.val != reverse.val:
        #         return False
        #     curr = curr.next
        #     reverse = reverse.next

        # return True


# @lc code=end
