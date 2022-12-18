# Copyright (C) Suresh Kumar Srivastava - All Rights Reserved
# DSA Masterclass courses are available on CourseGalaxy.com

# undirected_graph.py : Program for traversing an undirected graph through DFS.
# Visiting only those vertices that are reachable from start vertex.
# Visiting all vertices

from queue import LifoQueue

INITIAL = 0
VISITED = 1

class Vertex:
	def __init__(self, name):
		self.name = name
		self.state = None

class UndirectedGraph:
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
			self._adj[v][u] = 1
			self._nedges += 1

	def display(self):
		for i in range(self._nvertices):
			for j in range(self._nvertices):
				print(self._adj[i][j], end=" ")
			print()

	def _is_adjacent(self, u, v):
		return self._adj[u][v] != 0

	def _dfs(self, vertex):
		dfs_stack = LifoQueue()
		
		# Push the start vertex into stack
		dfs_stack.put(vertex)
		
		while dfs_stack.qsize() != 0:
			vertex = dfs_stack.get()
			
			if self._vertex_list[vertex].state == INITIAL:
				self._vertex_list[vertex].state = VISITED
				print(self._vertex_list[vertex].name, end=" ")

			# Looking for the adjacent vertices of the popped element, and from these push only those vertices into the stack
			# which are in the INITIAL state.
			for i in range(self._nvertices-1,-1,-1):
				# Checking for adjacent vertices with INITIAL state
				if self._is_adjacent(vertex,i) and self._vertex_list[i].state==INITIAL:
					dfs_stack.put(i)
		print()
	
	def dfs_traversal(self, vertex_name):
		# Initially all the vertices will have INITIAL state
		for i in range(self._nvertices):
			self._vertex_list[i].state = INITIAL
		
		self._dfs(self._get_index(vertex_name))
		
	def dfs_traversal_all(self, vertex_name):
		# Initially all the vertices will have INITIAL state
		for i in range(self._nvertices):
			self._vertex_list[i].state = INITIAL
		
		self._dfs(self._get_index(vertex_name))
		
		for v in range(self._nvertices):
			if self._vertex_list[v].state == INITIAL:
				self._dfs(v)
		
if __name__ == '__main__':
	
	u_graph = UndirectedGraph()

	try:
		# Creating the graph, inserting the vertices and edges
		u_graph.insert_vertex("0")
		u_graph.insert_vertex("1")
		u_graph.insert_vertex("2")
		u_graph.insert_vertex("3")
		u_graph.insert_vertex("4")
		u_graph.insert_vertex("5")
		u_graph.insert_vertex("6")
		u_graph.insert_vertex("7")
		u_graph.insert_vertex("8")
		u_graph.insert_vertex("9")
		u_graph.insert_vertex("10")
		u_graph.insert_vertex("11")
		u_graph.insert_vertex("12")
		u_graph.insert_vertex("13")
		u_graph.insert_vertex("14")

		u_graph.insert_edge("0","1")
		u_graph.insert_edge("0","2")
		u_graph.insert_edge("0","3")
		u_graph.insert_edge("2","3")

		u_graph.insert_edge("4","5")
		u_graph.insert_edge("4","6")
		u_graph.insert_edge("4","7")
		u_graph.insert_edge("4","8")
		u_graph.insert_edge("5","7")
		u_graph.insert_edge("6","8")
		u_graph.insert_edge("6","9")

		u_graph.insert_edge("10","11")
		u_graph.insert_edge("10","12")
		u_graph.insert_edge("10","13")
		u_graph.insert_edge("11","12")
		u_graph.insert_edge("11","13")
		u_graph.insert_edge("11","14")
		u_graph.insert_edge("13","14")

		# Display the graph
		u_graph.display()
		print()
		
		# DFS traversal visiting only those vertices that are reachable from start vertex
		u_graph.dfs_traversal("0")

		# DFS traversal visiting all the vertices
		u_graph.dfs_traversal_all("0")
		
	except Exception as e:
		print(e)
		
