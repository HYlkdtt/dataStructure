class Heap:
    def __init__(self, iterable=None):
        if iterable:
            self.data = list(iterable)
            self._heapify()
        else:    
            self.data = []
    
    def __len__(self):
        return len(self.data)
    
    def push(self, val):
        self.data.append(val)
        self._siftUp(len(self.data)-1)
    
    def pop(self):
        if not self.data:
            return False
        root = self.data[0]
        last = self.data.pop()

        if self.data:
            self.data[0] = last
            self._siftDown(0)
        
        return root
    
    def peek(self):
        if not self.data:
            return False
        return self.data[0]

    def _parent(self, i):
        return (i-1)//2
    
    def _left(self, i):
        return 2*i+1
    
    def _right(self, i):
        return 2*i+2

    def _siftUp(self, i):
        while i > 0 and self.data[i] < self.data[self._parent(i)]:
            parentIndex = self._parent(i)
            self.data[i], self.data[parentIndex] = self.data[parentIndex], self.data[i]
            i = parentIndex
        
    def _siftDown(self, i):
        while self._left(i) < len(self.data):
            if self._right(i) < len(self.data):
                sChild = self._left(i) if self.data[self._left(i)] < self.data[self._right(i)] else self._right(i)
            else:
                sChild = self._left(i)
            
            if self.data[i] > self.data[sChild]:
                self.data[i], self.data[sChild] = self.data[sChild], self.data[i]
                i = sChild
            else:
                break
            

    def _heapify(self):
        n = len(self.data)
        
        for i in range(n//2-1, -1, -1):
            self._siftDown(i)

