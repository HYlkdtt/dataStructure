class Node:
  def __init__(self, val=0):
    self.val = val
    self.next = None

class Stack:
  def __init__(self):
    self.height = 0
    self.top = None

  def printStack(self):
    ptr = self.top
    while ptr:
      print(ptr.val)
      ptr = ptr.next

  def push(self, val):
    node = Node(val)
    node.next = self.top
    self.top = node
    self.height += 1

  def pop(self):
    if not self.top:
      return None

    temp = self.top
    self.top = temp.next
    self.height -= 1
    return temp.val
