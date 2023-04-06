#
# @lc app=leetcode id=138 lang=python
#
# [138] Copy List with Random Pointer
#

# @lc code=start

# Definition for a Node.
# class Node:
#     def __init__(self, x, next=None, random=None):
#         self.val = int(x)
#         self.next = next
#         self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        # Using A LOT of extra memory!!
        headNew = Node(0, None, None)

        mArr = []
        mDict = {}

        curr = head
        currNew = headNew
        while curr:
            # new list
            next = Node(curr.val, None, None)
            currNew.next = next

            # mArr = random pointers
            mArr.append(curr.random)

            # mapping old with new
            mDict[curr] = next

            currNew = currNew.next
            curr = curr.next

        index = 0
        curr = headNew.next
        while curr:
            curr.random = mDict[mArr[index]] if mArr[index] else None
            curr = curr.next
            index += 1

        return headNew.next


# @lc code=end
