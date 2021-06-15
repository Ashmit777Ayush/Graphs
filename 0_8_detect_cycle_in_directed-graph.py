import threading
# directed graph
class Graph:
    def __init__(self, vertex):
        # vertex of the graph
        self.vertex = vertex

        # adjacent list
        self.adjList = [[] for x in range(vertex)]

        # visited
        self.visit = [False for x in range(vertex)]

        # stack to check for the cycle
        self.stack = [False for x in range(vertex)]

        # mark when going through checking whether the given graph having cycle or not
        self.cycle = False

    # explore a particular vertex
    def Explore(self, vertex):
        # mark the vertex as visited
        self.visit[vertex]=True

        # make the stack of this vertex as true
        self.stack[vertex]=True

        # now explore the neighbours of the vertex
        for ver in  self.adjList[vertex]:
            # if not visited then explore it
            if self.visit[ver]==False:
                self.Explore(ver)
            # if not visited and then it is in the stack then it makes  the cycle
            elif self.stack[ver]==True:
                self.cycle=True
                return 
            else:
                pass

        # now if we have explored then we need to mark down from True to False of that vertex in te self.stack
        self.stack[vertex]=False


    # dfs
    def dfs(self):
        for vertex in range(self.vertex):
            # check if not visisted that is explored then explore that particualr vertex
            if self.visit[vertex]==False:
                self.Explore(vertex)


    # add edges
    def addEdge(self, vertex1, vertex2):
        self.adjList[vertex1].append(vertex2)

def main():
    # number of vertices and edges
    vertex, edge = [int(x) for x in input().split()]

    # graph 
    graph = Graph(vertex)

    # assign the edges of the graph
    for x in range(edge):
        vertex1, vertex2 = [int(y) for y in input().split()]
        # add this edge
        graph.addEdge(vertex1, vertex2)

    # do dfs to detect the cycle
    graph.dfs()
    
    print("Graph is having the cycle") if graph.cycle==True else print("Graph do not contains the cycle")

threading .Thread(target=main).start()

    
'''
tets case
input
4 6
0 1
0 2
1 2
2 0
2 3
3 3

output
Graph is having the cycle
'''
