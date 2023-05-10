#
# @lc app=leetcode id=102 lang=python
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    

    def levelOrder(self, root):

        if not root:
            return 
        
        stack = [root]
        res = []

        while stack:
            temp = []

            for _ in range(len(stack)):

                node = stack.pop(0)

                if node:
                    temp.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)

            if len(temp) > 0:
                res.append(temp)

        return res
    

    # def __init__(self) :
    #     self.queue = []

    # def levelOrder(self, root):

    #     if type(root) == list:
    #         if len(root) == 0:
    #             return
    #     else:
    #         if not root:
    #             return
    #         root = [root]
        
    #     self.queue.append(root)

    #     def getChildNodes(nodes):
    #         childNodes = []
    #         for parent in nodes:
    #             if parent.left:
    #                 childNodes.append(parent.left)
    #             if parent.right:
    #                 childNodes.append(parent.right)
                
    #         return childNodes
        
    #     self.levelOrder(getChildNodes(self.queue[-1]))
        
    #     return [[n.val for n in nodes] for nodes in self.queue]

    


        
# @lc code=end

