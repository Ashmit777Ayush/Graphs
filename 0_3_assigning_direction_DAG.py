# python3
import threading
class Graph:
    def __init__(self):
        self.adj_list = {}# for the asjacency list
        self.visited = []# whether visited or not
        self.post = []# for the topological order

    def dfs(self):
        # do depth first search
        for vertex in self.adj_list.keys():
            if self.visited[vertex]==False:# if not visited then on;ly explore
                self.explore(vertex)

    def explore(self, vertex):
        self.visited[vertex]=True
        # print(vertex)

        for ver in self.adj_list[vertex] :# for every edge
            if self.visited[ver]==False and vertex not in self.adj_list[ver]:# check if undirected then not explore that edge
                self.explore(ver)
            

        self.postOrder(vertex) # do postorder for the topological sort

    # for storiing the postorder
    def postOrder(self, vertex):
        self.post.append(vertex)

    # asssigning directions by deleteing the edges 
    def assignDirection(self):
        # print(self.post, self.post[::-1])
        for vertex1 in self.post[::-1]:# for every vertex in topological order
            for vertex2 in self.adj_list[vertex1]:# edge edge
                if vertex1 in self.adj_list[vertex2]:# if undirectional then 
                    self.adj_list[vertex2].remove(vertex1)# delete the reverse direction as in the direction of topological order edges can only make the graph Directed Acyclic Graph
                    print('directed  edge new -->\t', vertex1,'-->',vertex2)
    # printing all the
    def printAllEdges(self):
        for vertex1 in self.adj_list.keys():
            if len(self.adj_list[vertex1]):
                for vertex2 in self.adj_list[vertex1]:
                    print(vertex1, '-->', vertex2, end='\t\t')

        print(end='\n')


def main():
    num_vertex = int(input('number of vertex -->\t'))
    graph = Graph()

    for x in range(num_vertex):
        graph.adj_list[x]=set()
        graph.visited.append(False)

    # for directed edges
    directed = int(input('number of directed edge -->\t'))
    for z in range(directed):
        vertex1, vertex2 = [int(x) for x in input('vertex1  vertex2 -->\t').split()]
        graph.adj_list[vertex1].add(vertex2)

    # for undiretced edges
    undirected = int(input('number of undirected edges -->\t'))
    for z in range(undirected):
        vertex1, vertex2 = [int(x) for x in input('vertex1 vertex2 -->\t').split()]

        # as it is undirected so both direction 
        graph.adj_list[vertex1].add(vertex2)
        graph.adj_list[vertex2].add(vertex1)
    
    # print(*graph.adj_list.items())
    graph.dfs()# for having topological sort
    graph.assignDirection()# assigning direcion
    graph.printAllEdges()

threading.Thread(target=main).start()
