class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
    def append(self, val):
        temp = Node(val)
        
        # 1. Edge Case: Empty list
        if not self.head:
            self.head = temp
            self.tail = temp
            self.size += 1
            return None

        # Regular append at the back
        self.tail.next = temp
        temp.prev = self.tail
        self.tail = temp
        self.size += 1

    def pop(self):
        # 1. Edge Case: Empty list
        if not self.head:
            return None
        
        # 2. Edge Case: Only one node in the list
        if self.size == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return temp.val

        # Regular pop at the end
        temp = self.tail
        self.tail = temp.prev
        self.tail.next = None
        self.size -= 1
        return temp.val

    def prepend(self, val):
        temp = Node(val)

        # 1. Edge Case: Empty list
        if not self.head:
            self.head = temp
            self.tail = temp
            self.size += 1
            return None
        
        # Regular Case
        temp.next = self.head
        self.head.prev = temp
        self.head = temp
        self.size += 1

    def popFirst(self):
        # 1. Edge Case: Empty list
        if not self.head:
            return None
        
        # 2. Edge Case: Only one node 
        if self.size == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return temp.val
        
        # Regular Case
        temp = self.head
        self.head = temp.next
        self.head.prev = None
        self.size -= 1
        return temp.val

    def get(self, index):
        # Check index range
        if index < 0 or index >= self.size:
            return None
        
        mid = self.size // 2
        # Node at the first half
        if index < mid:
            ptr = self.head
            for _ in range(index):
                ptr = ptr.next
            return ptr.val

        # Node at the second half
        else:
            ptr = self.tail
            for _ in range(self.size-index-1):
                ptr = ptr.prev
            return ptr.val

    def setValue(self, index, val):
        # Check index range
        if index < 0 or index >= self.size:
            return None
        
        mid = self.size // 2
        # Node at the first half
        if index < mid:
            ptr = self.head
            for _ in range(index):
                ptr = ptr.next
            ptr.val = val
        
        # Node at the second half
        else:
            ptr = self.tail
            for _ in range(self.size-index-1):
                ptr = ptr.prev
            ptr.val = val
    
    def insert(self, index, val):
        # Check index range
        if index < 0 or index > self.size:
            return None

        # 1. Edge Case: Prepend
        if index == 0:
            self.prepend(val)
            return None
            
        # 2. Edge Case: Append
        if index == self.size:
            self.append(val)
            return None

        # Regular Case
        mid = self.size // 2
        node = Node(val)
        if index < mid:
            ptr = self.head
            for _ in range(index):
                ptr = ptr.next
            node.prev = ptr.prev
            node.next = ptr
            ptr.prev.next = node
            ptr.prev = node

        else:
            ptr = self.tail
            for _ in range(self.size-1-index):
                ptr = ptr.prev
            node.prev = ptr.prev
            node.next = ptr
            ptr.prev.next = node
            ptr.prev = node
        
        self.size += 1
        return None

    def remove(self, index):
        # Check index range
        if index < 0  or index >= self.size:
            return None

        # 1. Edge Case: popFirst
        if index == 0:
            self.popFirst()
            return None

        # 2. Edge Case: pop
        if index == self.size - 1：
            self.pop()
            return None

        
        # Regular Case
        mid = self.size // 2
        if index < mid:
            ptr = self.head
            for _ in range(index):
                ptr = ptr.next
            ptr.prev.next = ptr.next
            ptr.next.prev = ptr.prev

        else:
            ptr = self.tail
            for _ in range(self.size-1-index):
                ptr = ptr.prev
            ptr.prev.next = ptr.next
            ptr.next.prev = ptr.prev

        self.size -= 1
        return None    
        

