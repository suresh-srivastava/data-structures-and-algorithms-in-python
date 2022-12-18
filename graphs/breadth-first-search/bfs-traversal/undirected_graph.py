# Copyright (C) Suresh Kumar Srivastava - All Rights Reserved
# DSA Masterclass courses are available on CourseGalaxy.com

# undirected_graph.py : Program for traversing an undirected graph through BFS.
# Visiting only those vertices that are reachable from start vertex.
# Visiting all vertices.
# Finding graph is connected or not connected.

from queue import Queue

INITIAL = 0
WAITING = 1
VISITED = 2

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
		
	def _bfs(self, vertex):
		bfs_queue = Queue()
		
		# Inserting the start vertex into queue and changing its state to WAITING
		bfs_queue.put(vertex)
		self._vertex_list[vertex].state = WAITING
		
		while bfs_queue.qsize() != 0:
			# Deleting front element from the queue and changing its state to VISITED
			vertex = bfs_queue.get()
			self._vertex_list[vertex].state = VISITED
			
			print(self._vertex_list[vertex].name, end=" ")
			
			# Looking for the adjacent vertices of the deleted element, and from these insert only those vertices into the
			# queue which are in the INITIAL state. Change the state of all these inserted vertices from INITIAL to WAITING
			for i in range(self._nvertices):
				# Checking for adjacent vertices with INITIAL state
				if self._is_adjacent(vertex,i) and self._vertex_list[i].state==INITIAL:
					bfs_queue.put(i)
					self._vertex_list[i].state = WAITING
		print()

	def bfs_traversal(self, vertex_name):
		# Initially all the vertices will have INITIAL state
		for i in range(self._nvertices):
			self._vertex_list[i].state = INITIAL
			
		self._bfs(self._get_index(vertex_name))

	def bfs_traversal_all(self, vertex_name):
		# Initially all the vertices will have INITIAL state
		for i in range(self._nvertices):
			self._vertex_list[i].state = INITIAL
			
		self._bfs(self._get_index(vertex_name))	
		
		for v in range(self._nvertices):
			if self._vertex_list[v].state == INITIAL:
				self._bfs(v)

	def is_connected(self):
		connected = True
		# Initially all the vertices will have INITIAL state
		for i in range(self._nvertices):
			self._vertex_list[i].state = INITIAL
			
		self._bfs(0) # Start traversal from vertex 0
		
		for v in range(self._nvertices):
			if self._vertex_list[v].state == INITIAL:
				connected = False
				break
		return connected
		
if __name__ == '__main__':
	
	u_graph = UndirectedGraph()
	
	try:
		# Creating the graph, inserting the vertices and edges
		# Connected Graph
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

		u_graph.insert_edge("0","1")
		u_graph.insert_edge("0","3")
		u_graph.insert_edge("1","2")
		u_graph.insert_edge("1","4")
		u_graph.insert_edge("1","5")
		u_graph.insert_edge("2","3")
		u_graph.insert_edge("2","5")
		u_graph.insert_edge("3","6")
		u_graph.insert_edge("4","7")
		u_graph.insert_edge("5","6")
		u_graph.insert_edge("5","7")
		u_graph.insert_edge("5","8")
		u_graph.insert_edge("6","9")
		u_graph.insert_edge("7","8")
		u_graph.insert_edge("8","9")

		# Not Connected Graph
		# u_graph.insert_vertex("0")
		# u_graph.insert_vertex("1")
		# u_graph.insert_vertex("2")
		# u_graph.insert_vertex("3")
		# u_graph.insert_vertex("4")
		# u_graph.insert_vertex("5")
		# u_graph.insert_vertex("6")
		# u_graph.insert_vertex("7")
		# u_graph.insert_vertex("8")
		# u_graph.insert_vertex("9")
		# u_graph.insert_vertex("10")
		# u_graph.insert_vertex("11")
		# u_graph.insert_vertex("12")
		# u_graph.insert_vertex("13")
		# u_graph.insert_vertex("14")

		# u_graph.insert_edge("0","1")
		# u_graph.insert_edge("0","3")
		# u_graph.insert_edge("1","2")
		# u_graph.insert_edge("2","3")

		# u_graph.insert_edge("4","5")
		# u_graph.insert_edge("4","7")
		# u_graph.insert_edge("4","8")
		# u_graph.insert_edge("5","6")
		# u_graph.insert_edge("5","8")
		# u_graph.insert_edge("6","9")
		# u_graph.insert_edge("7","8")
		# u_graph.insert_edge("8","9")

		# u_graph.insert_edge("10","11")
		# u_graph.insert_edge("10","13")
		# u_graph.insert_edge("10","14")
		# u_graph.insert_edge("11","12")
		# u_graph.insert_edge("12","13")
		# u_graph.insert_edge("13","14")
		
		# Display the graph
		u_graph.display()
		print()
		
		# BFS traversal visiting only those vertices that are reachable from start vertex
		u_graph.bfs_traversal("4")

		# BFS traversal visiting all the vertices
		u_graph.bfs_traversal_all("0")

		# Find out that graph is connected or not connected
		if u_graph.is_connected():
			print("Graph is connected")
		else:
			print("Graph is not connected")
		
	except Exception as e:
		print(e)
		
