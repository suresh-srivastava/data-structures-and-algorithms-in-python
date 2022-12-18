# Copyright (C) Suresh Kumar Srivastava - All Rights Reserved
# DSA Masterclass courses are available on CourseGalaxy.com

# undirected_weighted_graph.py : Program to create minimum spanning tree using prim's algorithm.

TEMPORARY = 0
PERMANENT = 1
INFINITY = 9999
NIL = -1

class Vertex:
	def __init__(self, name):
		self.name = name
		self.status = None
		self.predecessor = None
		self.length = None

class Edge:
	def __init__(self, u, v):
		self.u = u
		self.v = v

class UndirectedWeightedGraph:
	def __init__(self, max_size=30):
		self._nvertices = 0
		self._nedges = 0
		self._adj = [ [0 for column in range(max_size)] for row in range(max_size) ]		
		self._vertex_list = []
		self._tree_edges = []

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
			self._adj[v][u] = weight
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
			if self._vertex_list[i].status==TEMPORARY and self._vertex_list[i].length<min:
				min = self._vertex_list[i].length
				k = i
		
		return k

	def _prims_algorithm(self, r):
		count = 0	# Number of edges in the tree
		
		# Make all vertices temporary
		for i in range(self._nvertices):
			self._vertex_list[i].status = TEMPORARY
			self._vertex_list[i].predecessor = NIL
			self._vertex_list[i].length = INFINITY
		
		# Make length of source vertex equal to 0
		self._vertex_list[r].length = 0
		
		while True:
			# Search for temporary vertex with minimum length and make it current vertex
			current = self._get_minimum_temporary()
			
			if current == NIL:
				if count == self._nvertices-1:
					break	# No temporary vertex left
				else:		# Temporary vertices left with length INFINITY
					raise Exception("Graph is not connected, spanning tree is not possible.")

			# Make current vertex PERMANENT
			self._vertex_list[current].status = PERMANENT

			# Insert the edge (_vertex_list[current]->predecessor,current) into the tree,
			# except when the current vertex is root
			if current != r:
				count += 1
				self._tree_edges.append(Edge(self._vertex_list[current].predecessor,current))
				
			for v in range(self._nvertices):
				# Checks for adjacent temporary vertices
				if self._is_adjacent(current,v) and self._vertex_list[v].status==TEMPORARY:
					if self._adj[current][v] < self._vertex_list[v].length:
						self._vertex_list[v].predecessor = current	# Relabel
						self._vertex_list[v].length = self._adj[current][v]

	def minimum_spanning_tree(self, root):
		r = self._get_index(root)
		tree_weight = 0
		
		self._prims_algorithm(r)

		print("Root vertex : " + self._vertex_list[r].name)
		
		print("Minimum Spanning Tree Edges :")
		for e in self._tree_edges:
			print("Edge - (" + self._vertex_list[e.u].name + "-" + self._vertex_list[e.v].name + ")")
			tree_weight += self._adj[e.u][e.v]

		print("Minimum Spanning Tree Weight :", tree_weight)
		
if __name__ == '__main__':
	
	uw_graph = UndirectedWeightedGraph()
	
	try:
		# Creating the graph, inserting the vertices and edges
		# Connected graph
		uw_graph.insert_vertex("0")
		uw_graph.insert_vertex("1")
		uw_graph.insert_vertex("2")
		uw_graph.insert_vertex("3")
		uw_graph.insert_vertex("4")
		uw_graph.insert_vertex("5")

		uw_graph.insert_edge("0","1",6)
		uw_graph.insert_edge("0","2",2)
		uw_graph.insert_edge("0","3",3)
		uw_graph.insert_edge("0","4",10)
		uw_graph.insert_edge("1","3",11)
		uw_graph.insert_edge("1","5",9)
		uw_graph.insert_edge("2","3",14)
		uw_graph.insert_edge("2","4",8)
		uw_graph.insert_edge("3","4",7)
		uw_graph.insert_edge("3","5",5)
		uw_graph.insert_edge("4","5",4)

		# Not connected graph
		# uw_graph.insert_vertex("0")
		# uw_graph.insert_vertex("1")
		# uw_graph.insert_vertex("2")
		# uw_graph.insert_vertex("3")
		# uw_graph.insert_vertex("4")
		# uw_graph.insert_vertex("5")
		# uw_graph.insert_vertex("6")
		# uw_graph.insert_vertex("7")

		# uw_graph.insert_edge("0","1",6)
		# uw_graph.insert_edge("0","2",3)
		# uw_graph.insert_edge("0","3",8)
		# uw_graph.insert_edge("1","4",9)
		# uw_graph.insert_edge("2","3",7)
		# uw_graph.insert_edge("2","4",5)
		# uw_graph.insert_edge("3","4",4)

		# uw_graph.insert_edge("5","6",2)
		# uw_graph.insert_edge("5","7",8)
		# uw_graph.insert_edge("6","7",5)
		
		# Display the graph
		uw_graph.display()
		print()
		
		uw_graph.minimum_spanning_tree("0")
		
	except Exception as e:
		print(e)
		
