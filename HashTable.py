class HastTable:
    def __init__(self, size = 7):
        self.dataMap = [None] * size
    
    def __hash(self, key):
        myHash = 0
        for letter in key:
            myHash = (myHash + ord(letter) * 23) % len(self.dataMap)
        return myHash

    def printTable(self):
        for i, val in enumerate(self.dataMap):
            print(i, ":", val)

    def setItem(self, key, value):
        index = self.__hash(key)

        if not self.dataMap[index]:
            self.dataMap[index] = []

        self.dataMap[index].append([key, value])

    def getItem(self, key):
        index = self.__hash(key)

        if not self.dataMap[index]:
            return None
        
        for itemPair in self.dataMap[index]:
            if itemPair[0] == key:
                return itemPair[1]
        
        return None
    
    def keys(self):
        allKeys = []

        for item in self.dataMap:
            if item:
                for pair in item:
                    allKeys.append(pair[0])
        
        return allKeys
    