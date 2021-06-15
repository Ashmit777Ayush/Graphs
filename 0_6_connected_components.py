# undirected graph
import threading
class Graph:
    def __init__(self, ver):
        # umber of vertices
        self.ver = ver
        # adjacency list
        self.adjList = [[] for x in range(ver)]
        # connexted componenets tracker
        self.connectedComp = []
        # visited or not
        self.visited = [False for x in range(ver)]

    # add edges to the undirected graph
    def addEdge(self, vertex1, vertex2):
        # for undirected graph
        self.adjList[vertex1].append(vertex2)
        self.adjList[vertex2].append(vertex1)

    # explore a particular vertex
    def Explore(self, vertex, connected):
        # make it visited
        self.visited[vertex]=True
        # mark the connected componenet
        connected.append(vertex)

        # now check it's neighbour
        for ver in self.adjList[vertex]:
            if self.visited[ver]==False:
                self.Explore(ver, connected)
        # return this list
        return connected

    # DFS
    def DFS(self):
        for vertex in range(self.ver):
            if self.visited[vertex]==False:
                # of the particular counter componenet
                connected = []
                self.Explore(vertex, connected)
                # now add the connected 
                self.connectedComp.append(connected)

def main():
    vertex, edges = [int(x) for x in input('vertex and edges -->\t').split()]

    graph = Graph(vertex)

    for x in range(edges):
        vertex1, vertex2 = [int(y) for y in input().split()]
        graph.addEdge(vertex1, vertex2)

    # call the dfs
    graph.DFS()

    for conn in graph.connectedComp:
        print(*conn)
threading.Thread(target=main).start()

'''
test case

input
5 3
1 0
2 3
3 4

output
0 1
2 3 4

input
8 6
0 4
1 4
2 6
3 1
3 4
5 7

output
0 4 1 3
2 6
5 7
'''
