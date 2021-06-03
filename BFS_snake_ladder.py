# python3
import threading
from collections import deque
class Graph:
    def __init__(self):
        self.distance = []# for the distance of the particular vertex
        self.total_vertex = None# total vrtex in the snake ladder game
        self.jump = []# if any jump up by lader or jump down by snake
        self.visited = []# if visited or not

    def snakeLadder(self, start):
        queue = deque()# have the deque
        queue.append(start)# first push the start vertex
        self.distance[start]=0

        while(len(queue)):
            vertex = queue.popleft()

            # at this we already have reached then break
            if vertex == self.total_vertex-1:
                break
            
            # the key is that from a dice we can jump from 1 to 6 at one throw 
            # so we will check from 1 t 6 distance
            newVertex = vertex+1

            while newVertex<=vertex+6 and newVertex<self.total_vertex:# as it might happen that last vertex is reached
                # if not visisted then go and check
                if self.visited[newVertex]==False:
                    # for all vertex +1 to vertex+6 distance would be +1 because at one move from dice we can go from 1 to 6 so distance from start will increase that is number of moves to get at this place would be only incemenbt 1 from that of the vertex move
                    self.visited[newVertex]=True

                    # now check whetehr we can jump up or down from here
                    # either we will append extra or newNode
                    if self.jump[newVertex]!=-1:
                        # we go either up or down, we can't remain at this vertex so append that vertex
                        extra = self.jump[newVertex]
                        self.distance[extra]=self.distance[newVertex]
                        queue.append(extra)
                        self.distance[extra]=self.distance[vertex]+1
                    else:
                        self.distance[newVertex]=self.distance[vertex]+1
                        queue.append(newVertex)
                # also check all the other possibilites from 1 to 6
                newVertex+=1



def main():
    vertex_number = int(input('give the total blocks of the ludo -->\t'))

    graph = Graph()
    graph.total_vertex=vertex_number
    for x in range(vertex_number):
        graph.distance.append(None)# distance as the None
        graph.jump.append(-1)# jump -1
        graph.visited.append(False)# all visted false initially


    number_of_moves = int(input('give the number of moves to be inserted -->\t'))# total extra movers or jump

    for z in range(number_of_moves):
        # from where to whre
        start, end = [int(x) for x in input('vertex1  vertex2 --> \t').split()]

        # as we are storing in the for of the 0 to vertex-1
        graph.jump[start-1]=end-1

    # place where to start
    start_index = int(input('from where to reach end -->\t'))

    # call the function to check
    graph.snakeLadder(start_index-1)# -1 beaacuse of 0 to v-1

    print(graph.distance[-1])

        

threading.Thread(target=main).start()
