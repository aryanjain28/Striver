#
# @lc app=leetcode id=208 lang=python
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start

# class TrieNode():
#     def __init__(self):
#         self.children = {}
#         self.word = False

class Trie(object):

    def __init__(self):
        self.children = {}
        
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        children = self.children
        for c in word:
            if c not in children:
                children[c] = {}
            children = children[c]
        children["#"] = 1
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        children = self.children
        for c in word:
            if c not in children:
                return False
            children = children[c]
        return "#" in children
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        children = self.children
        for c in prefix:
            if c not in children:
                return False
            children = children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

