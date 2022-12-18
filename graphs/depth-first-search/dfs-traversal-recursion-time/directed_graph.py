# Copyright (C) Suresh Kumar Srivastava - All Rights Reserved
# DSA Masterclass courses are available on CourseGalaxy.com

# directed_graph.py : Program for traversing a directed graph through DFS using recursion.
# Visiting only those vertices that are reachable from start vertex.
# Visiting all vertices
# Finding discovery time and finishing time of each vertex.

INITIAL = 0
VISITED = 1
FINISHED = 2

class Vertex:
	def __init__(self, name):
		self.name = name
		self.state = None
		self.discovery_time = None
		self.finishing_time = None

class DirectedGraph:
	time = None
	
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

	def insert_edge(self, source, destination):
		u = self._get_index(source)
		v = self._get_index(destination)

		if u == v:
			print("Not a valid edge")
		elif self._adj[u][v] != 0:
			print("Edge already present")
		else:
			self._adj[u][v] = 1
			self._nedges += 1

	def display(self):
		for i in range(self._nvertices):
			for j in range(self._nvertices):
				print(self._adj[i][j], end=" ")
			print()

	def _is_adjacent(self, u, v):
		return self._adj[u][v] != 0

	def _dfs(self, vertex):
		print(self._vertex_list[vertex].name, end=" ")
		self._vertex_list[vertex].state = VISITED
		DirectedGraph.time += 1
		self._vertex_list[vertex].discovery_time = DirectedGraph.time	# discovery time

		for i in range(self._nvertices):
			# Checking for adjacent vertices with INITIAL state
			if self._is_adjacent(vertex,i) and self._vertex_list[i].state==INITIAL:
				self._dfs(i)
		
		self._vertex_list[vertex].state = FINISHED
		DirectedGraph.time += 1
		self._vertex_list[vertex].finishing_time = DirectedGraph.time	# finishing time
	
	def dfs_traversal(self, vertex_name):
		# Initially all the vertices will have INITIAL state
		for i in range(self._nvertices):
			self._vertex_list[i].state = INITIAL
		
		DirectedGraph.time = 0
		self._dfs(self._get_index(vertex_name))
		print()
		
	def dfs_traversal_all(self, vertex_name):
		# Initially all the vertices will have INITIAL state
		for i in range(self._nvertices):
			self._vertex_list[i].state = INITIAL
		
		DirectedGraph.time = 0
		self._dfs(self._get_index(vertex_name))
		
		for v in range(self._nvertices):
			if self._vertex_list[v].state == INITIAL:
				self._dfs(v)
		print()
		
		for v in range(self._nvertices):
			print("Vertex :", self._vertex_list[v].name, end=" ")
			print("Discovery Time :", self._vertex_list[v].discovery_time, end=" ")
			print("Finishing Time :", self._vertex_list[v].finishing_time)

if __name__ == '__main__':
	
	d_graph = DirectedGraph()
	
	try:
		# Creating the graph, inserting the vertices and edges
		d_graph.insert_vertex("0")
		d_graph.insert_vertex("1")
		d_graph.insert_vertex("2")
		d_graph.insert_vertex("3")
		d_graph.insert_vertex("4")
		d_graph.insert_vertex("5")
		d_graph.insert_vertex("6")
		d_graph.insert_vertex("7")
		d_graph.insert_vertex("8")

		d_graph.insert_edge("0","1")
		d_graph.insert_edge("0","3")
		d_graph.insert_edge("1","2")
		d_graph.insert_edge("1","4")
		d_graph.insert_edge("3","4")
		d_graph.insert_edge("3","6")
		d_graph.insert_edge("4","2")
		d_graph.insert_edge("4","5")
		d_graph.insert_edge("4","7")
		d_graph.insert_edge("6","7")
		d_graph.insert_edge("7","5")
		d_graph.insert_edge("7","8")
		
		# Display the graph
		d_graph.display()
		print()
		
		# DFS traversal visiting only those vertices that are reachable from start vertex
		d_graph.dfs_traversal("4")

		# DFS traversal visiting all the vertices
		d_graph.dfs_traversal_all("0")
		
	except Exception as e:
		print(e)
		
