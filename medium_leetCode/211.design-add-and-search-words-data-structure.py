#
# @lc app=leetcode id=211 lang=python
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class WordDictionary(object):

    def __init__(self):
        self.child = {}

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.child
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["#"] = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

        def find(node, word):
            for index, c in enumerate(word):
                if c == ".":
                    for key in dict.keys(node):
                        if key != "#" and find(node[key], word[index+1:]):
                            return True
                    return False
                elif c not in node:
                    return False
                node = node[c]
            return node.get("#", False)

        return find(self.child, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
