class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.Right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return None

        ptr = self.root
        while self.root:
            if val < ptr.val:
                ptr = ptr.left
