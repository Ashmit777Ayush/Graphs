import threading


class Graph:
    def __init__(self, vertex):
        # number of vertices
        self.vertices = vertex
        # adjList for the Graph
        self.adjList = [[] for x in range(vertex)]
        # visited
        self.visited = [False for x in range(vertex)]
        # pre
        self.pre = [-1 for x in range(vertex)]
        # post
        self.post = [-1 for x in range(vertex)]
        # counter 
        self.counter = 1

    # add edges
    def addEdge(self, vertex1, vertex2):
        self.adjList[vertex1].append(vertex2)
        self.adjList[vertex2].append(vertex1)
    # assign preorder
    def preOrder(self, vertex):
        self.pre[vertex]=self.counter
        self.counter+=1

    # assign postorder
    def postOrder(self, vertex):
        self.post[vertex]=self.counter
        self.counter+=1

    # explore 
    def Explore(self, vertex):
        # mark visited for this vertex as true
        self.visited[vertex]=True

        # add counter to preOrder
        self.preOrder(vertex)

        # now check it's neighbour
        for ver in self.adjList[vertex]:
            if self.visited[ver]==False:
                self.Explore(ver)

        # counter to the postOrder
        self.postOrder(vertex)

    
    # DFS
    def DFS(self):
        for vertex in range(self.vertices):
            if self.visited[vertex]==False:
                self.Explore(vertex)

def main():
    vertex, edges = [int(x) for x in input('vertex and edges --> \t').split()]

    graph = Graph(vertex)
    for x in range(edges):
        vertex1, vertex2 = [int(x) for x in input().split()]

        graph.addEdge(vertex1, vertex2)

    graph.DFS()

    print("pre-->\t", *graph.pre)
    print("post-->\t", *graph.post)

threading.Thread(target=main).start()

'''
test case
input
5 5
0 1
0 2
0 4
1 3
1 4

output
pre-->   1 2 8 3 5
post-->  10 7 9 4 6

'''
