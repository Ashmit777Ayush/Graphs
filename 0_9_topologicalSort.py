# directed a cyclc graph
import threading

class Graph:
    def __init__(self, vertex):
        # number of vertices
        self.vertices = vertex
        # adjacency list
        self.adjList = [[] for x in range(vertex)]
        # postOrder
        self.post = []
        # visit
        self.visit = [False for x in range(vertex)]

    # add edge
    def addEdge(self, vertex1, vertex2):
        self.adjList[vertex1].append(vertex2)

    # postVisit
    def postVisit(self, vertex):
        self.post.append(vertex)

    #  explore
    def Explore(self, vertex):
        #  first mark as visited 
        self.visit[vertex]=True

        # now check iyt's all neighbour
        for ver in self.adjList[vertex]:
            # now check visited or not
            if self.visit[ver]==False:
                self.Explore(ver)

        #  now assign this vertex in the postVisit
        self.postVisit(vertex)

    # dfs
    def dfs(self):
        for x in range(self.vertices):
            if self.visit[x]==False:
                self.Explore(x)


def main():
    vertex, edge = [int(x) for x in input().split()]

    graph = Graph(vertex)

    #  assign all the edges in the graph
    for x in range(edge):
        vertex1, vertex2 = [int(y) for y in input().split()]

        graph.addEdge(vertex1, vertex2)


    # do dfs
    graph.dfs()

    #  now reverse of the post is the topologivcal order
    graph.post.reverse()
    print(*graph.post)

threading.Thread(target=main).start()
'''
testcase

input
6 6
5 2
5 0
4 0
4 1
2 3
3 1
output
5 4 2 3 1 0
'''
