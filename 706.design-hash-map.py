#
# @lc app=leetcode id=706 lang=python
#
# [706] Design HashMap
#

# @lc code=start
class MyHashMap(object):

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = self.get(key)
        if index == -1:
            self.keys.append(key)
            self.values.append(value)
        else:
            self.keys[index] = key
            self.values[index] = key

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.keys:
            return self.values[self.keys.index(key)]
        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self.get(key)
        if index != -1:
            self.keys[index] = -1
            self.values[index] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end
