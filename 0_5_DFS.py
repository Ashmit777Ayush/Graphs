import threading
class Graph:
    def __init__(self, ver):
        # number of vertex
        self.vertex = ver
        # adjacency list
        self.adjList = [[] for x in range(ver)]
        # for marking visited or not during exploring vertices
        self.visited = [False for x in range(ver)]
        # add the element as visited next
        self.pre = [-1 for x in range(ver)]
        #  keep the counter
        self.countpre = 0

    # explore that particular vertex ver
    def Explore(self, ver):
        # mark it as the visited
        self.visited[ver]=True

        # for exploring in sequence  --> preorder
        self.pre[self.countpre] = ver
        self.countpre+=1# increase fro next iteration


        # explore if not visited inside that adjacency list of vertex ver
        for vertex in self.adjList[ver]:
            if self.visited[vertex]==False:
                self.Explore(vertex)

    # for the depth first search
    def DFS(self):
        # traverse through all the vertices
        for ver in range(self.vertex):
            # if not visited then explore it
            if self.visited[ver]==False:
                self.Explore(ver)


def main():
    vertex, edge = [int(x) for x in input('vertex and edges --> \t').split()]

    graph = Graph(vertex)

    for x in range(edge):
        ver1, ver2 = [int(x) for x in input().split()]

        # as it is undirected so we have to add it as the both direction 
        graph.adjList[ver1].append(ver2)
        graph.adjList[ver2].append(ver1)

    # now have the dfs
    graph.DFS()

    # print the explore vertices in te sequence
    print(*graph.pre)

threading.Thread(target=main).start()

'''
input
4 6
0 1
0 2
1 2
2 0
2 3
3 3

output
0 1 2 3



input
6 6
2 3
3 2
2 1
1 2
0 4
5 2
output
0 4 1 2 3 5


input
9 8
0 1
0 2
0 4
2 3
5 0
6 7
8 7
8 6

output
0 1 2 3 4 5 6 7 8
'''
