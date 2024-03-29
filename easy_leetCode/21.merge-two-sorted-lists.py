#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # New list
        # if list1 == None and list2 == None:
        #     return list1

        # head = new = ListNode()
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         new.val = list1.val
        #         list1 = list1.next
        #     else:
        #         new.val = list2.val
        #         list2 = list2.next

        #     new.next = ListNode()
        #     new = new.next

        # list = list1 if list1 != None else list2

        # new.val = list.val
        # new.next = list.next

        # return head

        # In place
        # if list1 == None:
        #     return list2

        # elif list2 == None:
        #     return list1

        # elif list1 == None and list2 == None:
        #     return list1

        # head = None
        # if list1.val <= list2.val:
        #     curr = list1
        #     other = list2
        # else:
        #     curr = list2
        #     other = list1

        # head = curr
        # while curr.next and other:

        #     if curr.next.val > other.val:
        #         # break and join other
        #         next = curr.next
        #         curr.next = other
        #         curr = other
        #         other = next

        #     else:
        #         curr = curr.next

        # curr.next = other
        # return head


# @lc code=end
