# python3
# using disjoint set to detect the cycle 
import threading
class Graph:
	def __init__(self, *args):
		self.edges = {}# for the edges
		self.set = [x for x in range(args[0])]# for the set-id of the elements
		self.rank = [x for x in range(args[0])]# for the rank of the particular element
	
	# find the set_id and also update it
	def find(self, i):
		if i!=self.set[i]:
			self.set[i]=self.find(self.set[i])
		
		return self.set[i]
	
	# union of the two element in set
	def union(self, *args):
		x = args[0]
		y = args[1]
		
		# get the set id's of both the vertex
		x_id = self.find(x)
		y_id = self.find(y)
		
		# if both belongs to same set then return
		if x_id==y_id:
			return
		else:
			# if rank of x_id is greater then  asiign x_id as set_id to the y_id
			if self.rank[x_id]>self.rank[y_id]:
				self.set[y_id]=x_id
			else:
				# if not then y_id as the set_id for the x_id
				self.set[x_id]=y_id
				
				# now check whether the both have the same rank or not
				if self.rank[x_id]==self.rank[y_id]:
					self.rank[y_id]+=1
					
					
	# check cycle
	def cycle(self):
		# traverse through each edge
		for ver1, ver2 in self.edges.items():
			# if not belongs to same set then union
			if self.find(ver1)!=self.find(ver2):
				self.union(ver1, ver2)
			else:# if belongs then cycle is deytected
				return True
		return False
		
def main():
	ver, edge = [int(x) for x in input('give number of vertex and edges --> \t').split()]
	graph = Graph(ver)
	for x in range(edge):
		ver1, ver2 = [int(x) for x in input('ver1 ve2 --> \t').split()]
		graph.graph[ver1]=ver2
		
	if graph.cycle():
		print('cycle is present in the graph')
	else:
		print('cycle is not present in the graph')
		
threading.Thread(target=main).start()
