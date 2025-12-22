class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return None

        ptr = self.root
        while ptr:
            if val < ptr.val:
                if not ptr.left:
                    ptr.left = Node(val)
                    return None
                ptr = ptr.left

            elif val > ptr.val:
                if not ptr.right:
                    ptr.right = Node(val)
                    return None
                ptr = ptr.right
            
            else:
                return None
        
        return None
        
    
    def contains(self, val):
        ptr = self.root
        while ptr:
            if val == ptr.val:
                return True

            elif val < ptr.val:
                ptr = ptr.left
            
            else:
                ptr = ptr.right

        return False
