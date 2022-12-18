# Copyright (C) Suresh Kumar Srivastava - All Rights Reserved
# DSA Masterclass courses are available on CourseGalaxy.com

# directed_weighted_graph.py : Program to find shortest paths using Dijkstra's algorithm.

TEMPORARY = 0
PERMANENT = 1
INFINITY = 9999
NIL = -1

class Vertex:
	def __init__(self, name):
		self.name = name
		self.status = None
		self.predecessor = None
		self.path_length = None

class DirectedWeightedGraph:
	def __init__(self, max_size=30):
		self._nvertices = 0
		self._nedges = 0
		self._adj = [ [0 for column in range(max_size)] for row in range(max_size) ]
		self._vertex_list = []

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

	def display(self):
		for i in range(self._nvertices):
			for j in range(self._nvertices):
				print(self._adj[i][j], end=" ")
			print()

	def _is_adjacent(self, u, v):
		return self._adj[u][v] != 0

	# Returns the temporary vertex with minimum value of path_length,
	# Returns NIL if no temporary vertex left or all temporary vertices left have path_length INFINITY
	def _get_minimum_temporary(self):
		min = INFINITY
		k = NIL
		
		for i in range(self._nvertices):
			if self._vertex_list[i].status==TEMPORARY and self._vertex_list[i].path_length<min:
				min = self._vertex_list[i].path_length
				k = i
		
		return k

	def _dijkstras_algorithm(self, s):
		# Make all vertices temporary
		for i in range(self._nvertices):
			self._vertex_list[i].status = TEMPORARY
			self._vertex_list[i].predecessor = NIL
			self._vertex_list[i].path_length = INFINITY
		
		# Make pathLength of source vertex equal to 0
		self._vertex_list[s].path_length = 0
		
		while True:
			# Search for temporary vertex with minimum pathLength and make it current vertex
			current = self._get_minimum_temporary()
			
			if current == NIL:
				break
				
			# Make current vertex PERMANENT
			self._vertex_list[current].status = PERMANENT
			
			for v in range(self._nvertices):
				# Checks for adjacent temporary vertices
				if self._is_adjacent(current,v) and self._vertex_list[v].status==TEMPORARY:
					if (self._vertex_list[current].path_length + self._adj[current][v]) < self._vertex_list[v].path_length:
						self._vertex_list[v].predecessor = current	# Relabel
						self._vertex_list[v].path_length = self._vertex_list[current].path_length + self._adj[current][v]

	def _find_path(self, s, v):
		path = []
		shortest_distance = 0
		u = None
		
		# Store the full path in the array path
		while v != s:
			path.append(v)
			u = self._vertex_list[v].predecessor
			shortest_distance += self._adj[u][v]
			v = u

		path.append(s)
		print("Shortest Path : ", end="")
		for u in reversed(path):
			print(self._vertex_list[u].name, end=" ")
		print()
		print("Shortest Distance :", shortest_distance)

	def find_paths(self, source):
		s = self._get_index(source)
		
		self._dijkstras_algorithm(s)
		
		print("Source :", source)
		
		for v in range(self._nvertices):
			print("Destination : " + self._vertex_list[v].name)
			if self._vertex_list[v].path_length == INFINITY:
				print("There is no path from " + source + " to vertex " + self._vertex_list[v].name)
			else:
				self._find_path(s, v)

if __name__ == '__main__':
	
	dw_graph = DirectedWeightedGraph()
	
	try:
		# Creating the graph, inserting the vertices and edges
		dw_graph.insert_vertex("0")
		dw_graph.insert_vertex("1")
		dw_graph.insert_vertex("2")
		dw_graph.insert_vertex("3")
		dw_graph.insert_vertex("4")
		dw_graph.insert_vertex("5")
		dw_graph.insert_vertex("6")
		dw_graph.insert_vertex("7")

		dw_graph.insert_edge("0","1",8)
		dw_graph.insert_edge("0","2",2)
		dw_graph.insert_edge("0","3",7)
		dw_graph.insert_edge("1","5",16)
		dw_graph.insert_edge("2","0",5)
		dw_graph.insert_edge("2","3",4)
		dw_graph.insert_edge("2","6",3)
		dw_graph.insert_edge("3","4",9)
		dw_graph.insert_edge("4","0",4)
		dw_graph.insert_edge("4","5",5)
		dw_graph.insert_edge("4","7",8)
		dw_graph.insert_edge("6","2",6)
		dw_graph.insert_edge("6","3",3)
		dw_graph.insert_edge("6","4",4)
		dw_graph.insert_edge("7","5",2)
		dw_graph.insert_edge("7","6",5)
		
		# Display the graph
		dw_graph.display()
		print()
		
		# Finding path from source vertex to other vertices
		dw_graph.find_paths("0")

	except Exception as e:
		print(e)
		
