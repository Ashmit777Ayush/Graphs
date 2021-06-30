class Graph:
    def __init__(self, vertex):
        # number of vertices
        self.vertex = vertex

        # adjacecy list
        self.adjList = [[] for x in range(vertex)]

        # reverse graph
        self.adjListReverse =  [[] for x in range(vertex)]

        # visited
        self.visited = [False for x in range(vertex)]

        # for post visit
        self.postVisit = []

        # for the strongly connected component
        self.scc = {}

        self.counter = 1


    # add the edge
    def addEdge(self, ver1, ver2):
        self.adjList[ver1].append(ver2)
        self.adjListReverse[ver2].append(ver1)


    # post order
    def post(self, vertex):
        print(vertex)
        self.postVisit.append(vertex)

    # explore Reverse
    def exploreRevrese(self, vertex):
        # mark as the vsited
        self.visited[vertex]=True

        # explore 
        for ver in self.adjListReverse[vertex]:
            if self.visited[ver]==False:
                self.exploreRevrese(ver)

        # postvisit
        self.post(vertex)


    # explore
    def explore(self, vertex):
        # mark as visited
        self.visited[vertex]=True
        

        # add to the SCC
        if self.counter in self.scc:
            self.scc[self.counter].append(vertex) 
        else:
            self.scc[self.counter]=[vertex]

        for ver in self.adjList[vertex]:
            if self.visited[ver]==False:
                self.explore(ver)


    # SCC 
    def SCC(self):
        # do dfs on the reverse graph and find the post order 
        # in post order the last element is the sourse
        # but as we are finding in the reverse graph it will be the source the last element of the postorder
        # so when we do dfs on the reverse of postorder of the reverse graph o the original graph then we will have the SCC
        for vertex in range(self.vertex):
            if self.visited[vertex]==False:
                self.exploreRevrese(vertex)

        # make all visited as the Fal;se
        for x in range(len(self.visited)):
            self.visited[x]=False

        
        # do dfs on the reverse on the post order
        # print(*self.postVisit)
        self.postVisit.reverse()
        # print(*self.postVisit)
        for vertex in self.postVisit:
            if self.visited[vertex]==False:
                self.explore(vertex)

                # increse the scc
                self.counter+=1

        
if __name__=="__main__":
    vertex, edge = [int(x) for x in input().split()]

    graph = Graph(vertex)


    for x in range(edge):
        ver1, ver2 = [int(x) for x in input().split()]
        graph.addEdge(ver1, ver2)

    # print(*graph.adjListReverse)
    # print(*graph.adjList)

    graph.SCC()

    for x, y in graph.scc.items():
        print(x, "\t-->\t", y)


        
'''
input 
5 5
1 0
0 2
2 1
0 3
3 4
output
1       -->      [4]
2       -->      [3]
3       -->      [0, 2, 1]


input
5 7
1 0
2 1
2 0
3 2
3 0
4 1
4 2
output
[0][1][2][4][3]
'''
