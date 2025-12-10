class Node:
	def __init__(self, val=0):
		self.val = val
		self.next = None

class SinglyLinkedList:
	def __init__(self):
		self.size = 0
		self.head = None

	def printList(self):
		ptr = self.head
		while ptr:
			print(ptr.val)
			ptr = ptr.next

	def append(self, val):
		# 1. Edge Case: Emtpy list
		if not self.head:
			self.head = Node(val)
			self.size += 1
			return None

		# Regular Append
		ptr = self.head
		while ptr.next:
			ptr = ptr.next
		ptr.next = Node(val)
		self.size += 1

	def pop(self):
		# 1. Edge Case: Empty list
		if not self.head:
			return None

		# 2. Edge Case: Only one node in the list
		if not self.head.next:
			val = self.head.val
			self.head = None
			self.size -= 1
			return val

		# 3. Regular pop
		ptr = self.head
		while ptr.next.next:
			ptr = ptr.next
		val = ptr.next.val
		ptr.next = None
		self.size -= 1
		return val

	def prepend(self, val):
		# 1. Edge Case: Empty list
		if not self.head:
			self.head = Node(val)
			self.size += 1
			return None

		# Regular prepend
		temp = Node(val)
		temp.next = self.head
		self.head = temp
		self.size += 1

	def popFirst(self):
		# 1. Edge Case: Empty list
		if not self.head:
			return None

		# Regular popFirst
		temp = self.head
		self.head = self.head.next
		self.size -= 1
		return temp.val
			
	def get(self, index):
		# index range validation
		if index < 0 or index >= self.size:
			return None

		# getting to the index
		ptr = self.head
		for _ in range(index):
			ptr = ptr.next
		return ptr.val

	def setValue(self, index, val):
		# index range validation
		if index < 0 or index >= self.size:
			return None

		# getting to the index
		ptr = self.head
		for _ in range(index):
			ptr = ptr.next
		ptr.val = val

	def insert(self, index, val):
		# index range validation
		if index < 0 or index > self.size:
			return None

		# 1. Edge Case: insert upfront
		if index == 0:
			return self.prepend(val)

		# 2. Edge Case: insert at end
		if index == self.size:
			return self.append(val)

		# getting to the index
		ptr = self.head
		for _ in range(index-1):
			ptr = ptr.next
		temp = ptr.next
		ptr.next = Node(val)
		ptr.next.next = temp
		self.size += 1

	def remove(self, index):
		# index range validation
		if index < 0 or index >= self.size:
			return None

		# 1. Edge Case: remove upfront
		if index == 0:
			self.popFirst()
			return None

		# 2. Edge Case: remove at end
		if index == self.size - 1:
			self.pop()
			return None

		# getting to the index
		ptr = self.head
		for _ in range(index-1):
			ptr = ptr.next
		ptr.next = ptr.next.next
		self.size -= 1

	def reverse(self):
		prev = None
		curr = self.head
		while curr:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		self.head = prev
			


			


