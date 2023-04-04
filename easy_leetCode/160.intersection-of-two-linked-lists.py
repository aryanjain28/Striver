#
# @lc app=leetcode id=160 lang=python
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x, next=None):
#         self.val = x
#         self.next = next


class Solution(object):

    def count(self, head):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        return count

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        # Using count
        countA = self.count(headA)
        countB = self.count(headB)

        diff = abs(countA - countB)

        if countA > countB:
            currA = headA
            currB = headB
        else:
            currA = headB
            currB = headA

        while diff > 0:
            currA = currA.next
            diff -= 1

        while currA != currB:
            currA = currA.next
            currB = currB.next

        return currA

        # Using extra memory. Set.
        # mSet = set()
        # # converting all the values in headB to -1
        # curr = headB
        # while curr:
        #     mSet.add(curr)
        #     curr = curr.next

        # # checking in headA if it encounters -1
        # curr = headA
        # while curr:
        #     if curr in mSet:
        #         return curr
        #     curr = curr.next

        # return None


# @lc code=end

# node = ListNode(5, None)
# head = ListNode(4, ListNode(1, ListNode(8, ListNode(4, node))))
# head = ListNode(1, ListNode(2, ListNode(6, ListNode(
#     3, ListNode(4, ListNode(5, ListNode(6, None)))))))
# Solution().getIntersectionNode(head, head)
