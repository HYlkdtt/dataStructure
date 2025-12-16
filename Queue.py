#Implemented through using a SinglyLinkedList with both head and tail
class Node:
  def __init__(self, val=0):
    self.val = val
    self.next = None

class Queue:
  def __init__(self):
    self.length = 0
    self.head = None
    self.tail = None

  def printQueue(self):
    ptr = self.head
    while ptr:
      print(ptr.val)
      ptr = ptr.next

  def enqueue(self, val):
    node = Node(val)

    # 1. Edge Case: Empty queue
    if not self.head:
      self.head = node
      self.tail = node
      self.length += 1
      return None

    # Regular Case
    self.tail.next = node
    self.tail = node
    self.length += 1
    

  def dequeue(self):
    # 1. Edge Case: Empty queue
    if not self.head:
      return None

    # 2. Edge Case: Only one node
    if self.length == 1:
      temp = self.head
      self.head = None
      self.tail = None
      self.length -= 1
      return temp.val

    # Regular Case
    temp = self.head
    self.head = temp.next
    self.length -= 1
    return temp.val
