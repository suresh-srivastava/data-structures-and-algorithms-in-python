# Copyright (C) Suresh Kumar Srivastava - All Rights Reserved
# DSA Masterclass courses are available on CourseGalaxy.com

# directed_weighted_graph.py : Program to find shortest path matrix by Modified Warshall's (Floyd) algorithm.

INFINITY = 9999

class Vertex:
	def __init__(self, name):
		self.name = name

class DirectedWeightedGraph:
	def __init__(self, max_size=30):
		self._nvertices = 0
		self._nedges = 0
		self._adj = [ [0 for column in range(max_size)] for row in range(max_size) ]
		self._vertex_list = []
		self._D = [ [0 for column in range(max_size)] for row in range(max_size) ]		# Shortest Path Matrix
		self._Pred = [ [0 for column in range(max_size)] for row in range(max_size) ]	# Predecessor Matrix

	def insert_vertex(self, vertex_name):
		self._vertex_list.append(Vertex(vertex_name))
		self._nvertices += 1
	
	def _get_index(self, vertex_name):
		index = 0
		for name in (vertex.name for vertex in self._vertex_list):
			if vertex_name == name:
				return index
			index += 1
		raise Exception("Invalid Vertex")

	def insert_edge(self, source, destination, weight):
		u = self._get_index(source)
		v = self._get_index(destination)

		if u == v:
			print("Not a valid edge")
		elif self._adj[u][v] != 0:
			print("Edge already present")
		else:
			self._adj[u][v] = weight
			self._nedges += 1

	def _display(self, mat):
		for i in range(self._nvertices):
			for j in range(self._nvertices):
				print(mat[i][j], end=" ")
			print()	
	
	def display(self):
		for i in range(self._nvertices):
			for j in range(self._nvertices):
				print(self._adj[i][j], end=" ")
			print()

	def _is_adjacent(self, u, v):
		return self._adj[u][v] != 0

	def _floyd_warshalls_algorithm(self, s):
		# Getting _D(-1), _Pred(-1)
		for i in range(self._nvertices):
			for j in range(self._nvertices):
				if self._adj[i][j] == 0:
					self._D[i][j] = INFINITY
					self._Pred[i][j] = -1
				else:
					self._D[i][j] = self._adj[i][j]
					self._Pred[i][j] = i
					
		# Getting _D(k), _Pred(k)
		for k in range(self._nvertices):
			for i in range(self._nvertices):
				for j in range(self._nvertices):
					if (self._D[i][k]+self._D[k][j]) < self._D[i][j]:
						self._D[i][j] = self._D[i][k]+self._D[k][j]
						self._Pred[i][j] = self._Pred[k][j]

		# Finding negative cycle
		for i in range(self._nvertices):
			if self._D[i][i] < 0:
				raise Exception("There is negative cycle in graph.")
		
		print("Shortest Path Matrix :")
		self._display(self._D)
		print("Predecessor Matrix :")
		self._display(self._Pred)

	def _find_path(self, s, v):
		path = []
		
		if self._D[s][v] == INFINITY:
			print("No path")
		else:
			while True:
				path.append(v)
				v = self._Pred[s][v]
				if v == s:
					break
		
			path.append(s)
			print("Shortest Path : ", end="")
			for u in reversed(path):
				print(self._vertex_list[u].name, end=" ")
			print()

	def find_paths(self, source):
		s = self._get_index(source)
		
		self._floyd_warshalls_algorithm(s)
		
		print("Source :", source)
		
		for v in range(self._nvertices):
			print("Destination : " + self._vertex_list[v].name)
			self._find_path(s, v)
			print("Shortest Distance :", self._D[s][v])

if __name__ == '__main__':
	
	dw_graph = DirectedWeightedGraph()
	
	try:
		# Creating the graph, inserting the vertices and edges
		dw_graph.insert_vertex("0")
		dw_graph.insert_vertex("1")
		dw_graph.insert_vertex("2")
		dw_graph.insert_vertex("3")

		dw_graph.insert_edge("0","1",2)
		dw_graph.insert_edge("0","3",9)
		dw_graph.insert_edge("1","0",3)
		dw_graph.insert_edge("1","2",4)
		dw_graph.insert_edge("1","3",7)
		dw_graph.insert_edge("2","1",6)
		dw_graph.insert_edge("2","3",2)
		dw_graph.insert_edge("3","0",14)
		dw_graph.insert_edge("3","2",4)

		# Graph with negative cycle
		# dw_graph.insert_vertex("0")
		# dw_graph.insert_vertex("1")
		# dw_graph.insert_vertex("2")
		# dw_graph.insert_vertex("3")
		# dw_graph.insert_vertex("4")

		# dw_graph.insert_edge("0","1",2)
		# dw_graph.insert_edge("0","2",7)
		# dw_graph.insert_edge("1","3",-9)
		# dw_graph.insert_edge("2","4",6)
		# dw_graph.insert_edge("3","0",4)
		# dw_graph.insert_edge("3","4",5)
		
		# Display the graph
		dw_graph.display()
		print()
		
		# Finding path from source vertex to other vertices
		dw_graph.find_paths("0")

	except Exception as e:
		print(e)
		
