#
# @lc app=leetcode id=133 lang=python
#
# [133] Clone Graph
#

class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# @lc code=start
# Definition for a Node.


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return None

        def backtrack(node):

            if node in created:
                return created[node]
            
            created[node] = Node(node.val)

            for neighbor in node.neighbors:
                created[node].neighbors.append(backtrack(neighbor))

            return created[node]
        

        created = {}
        return backtrack(node)


        # if not node:
        #     return None

        # mNode = Node(node.val)
        # queue = [(node, mNode)]
        # created = { node: mNode }

        # while queue:

        #     curr, mCurr = queue.pop(0)

        #     for n in curr.neighbors:
        #         if n not in created:
        #             created[n] = Node(n.val)
        #             queue.append((n, created[n]))

        #         mCurr.neighbors.append(created[n])

        # return mNode










        
# @lc code=end

