class Graph:
    def __init__(self):
        self.adjacencyList = {}
    
    def printGraph(self):
        for vertex in self.adjacencyList:
            print(vertex, ':', self.adjacencyList[vertex])
    
    def addVertex(self, vertex):
        if vertex not in self.adjacencyList.keys():
            self.adjacencyList[vertex] = []
            return True
        return False

    def addEdge(self, v1, v2):
        if v1 in self.adjacencyList.keys() and v2 in self.adjacencyList.keys() and v1 not in self.adjacencyList[v2] and v2 not in self.adjacencyList[v1]:
                self.adjacencyList[v1].append(v2)
                self.adjacencyList[v2].append(v1)
                return True
        return False
    
    def removeEdge(self, v1, v2):
        if v1 in self.adjacencyList.keys() and v2 in self.adjacencyList.keys() and v1 in self.adjacencyList[v2] and v2 in self.adjacencyList[v1]:
            self.adjacencyList[v1].remove(v2)
            self.adjacencyList[v2].remove(v1)
            return True
        return False
    
    def removeVertex(self, vertex):
        if vertex in self.adjacencyList.keys():
            for otherVertex in self.adjacencyList[vertex]:
                self.adjacencyList[otherVertex].remove(vertex)
            self.adjacencyList.pop(vertex)
            return True
        return False