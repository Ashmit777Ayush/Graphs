# undirected graph
import threading
class Graph:
    def __init__(self, v):
        # adjacency matrix
        self.adjList = [[] for x in range(v)]
        # for checking visiting vertex
        self.visited = [False for x in range(v)]

    def Explore(self, key):
        self.visited[key] = True

        # we are exploring that  vertex that is not visited in depth first ordering
        for vertex in self.adjList[key]:
            # for checking whether it is visited or not
            if self.visited[vertex]==False:
                self.Explore(vertex)

def main():
    # number of vertices and edges
    v, edges = [int(x) for x in  (input('number of vertices and edges -->\t').split())]
    graph = Graph(v)

    for x in range(edges):# adding the edges in the adjacency matrix
        ver1, ver2 = [int(y) for y in input().split()]
        # as of now we are considering it as the undiretced  graph so add in both cases
        graph.adjList[ver1].append(ver2)
        graph.adjList[ver2].append(ver1)


    # after adding take the vertices to be explored
    key = int(input('give the vertex to be explored-->\t'))

    if key < v:
        graph.Explore(key) 
        print("connected vertex to the vertex {} are --> \t".format(key))
        for x in range(v):
            print(x, '-->', graph.visited[x], end='\t')
    else:
        print('vertex out of bound')

threading.Thread(target=main).start()

'''
test case
input
4 6
0 1
0 2
1 2
2 0
2 3
3 3
2

output 
0 --> True      1 --> True      2 --> True      3 --> True


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
0

output
0 --> True      1 --> True      2 --> True      3 --> True      4 --> True     5 --> True     6 --> False      7 --> False     8 --> False


input
6 6
2 3
3 2
2 1
1 2
0 4
5 2
0

output
0 --> True      1 --> False     2 --> False     3 --> False     4 --> True     5 --> False
'''
