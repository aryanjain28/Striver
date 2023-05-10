class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def search(self, root, target):

        if not root:
            return False

        if self.val > target:
            return self.search(self.left, target)
        elif self.val < target:
            return self.search(self.right, target)
        else:
            return True
