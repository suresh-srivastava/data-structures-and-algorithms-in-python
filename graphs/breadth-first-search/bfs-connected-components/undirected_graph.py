# Copyright (C) Suresh Kumar Srivastava - All Rights Reserved
# DSA Masterclass courses are available on CourseGalaxy.com

# undirected_graph.py : Program to find connected components in an undirected graph.

from queue import Queue

INITIAL = 0
WAITING = 1
VISITED = 2

class Vertex:
	def __init__(self, name):
		self.name = name
		self.state = None
		self.component_number = None

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
		
	def _bfs(self, vertex, cn):
		bfs_queue = Queue()
		
		# Inserting the start vertex into queue and changing its state to WAITING
		bfs_queue.put(vertex)
		self._vertex_list[vertex].state = WAITING
		
		while bfs_queue.qsize() != 0:
			# Deleting front element from the queue and changing its state to VISITED
			vertex = bfs_queue.get()
			self._vertex_list[vertex].state = VISITED
			self._vertex_list[vertex].component_number = cn
			
			# Looking for the adjacent vertices of the deleted element, and from these insert only those vertices into the
			# queue which are in the INITIAL state. Change the state of all these inserted vertices from INITIAL to WAITING
			for i in range(self._nvertices):
				# Checking for adjacent vertices with INITIAL state
				if self._is_adjacent(vertex,i) and self._vertex_list[i].state==INITIAL:
					bfs_queue.put(i)
					self._vertex_list[i].state = WAITING

	def connected_component(self):
		component_number = 0
		# Initially all the vertices will have INITIAL state
		for i in range(self._nvertices):
			self._vertex_list[i].state = INITIAL
		
		component_number += 1
		self._bfs(0, component_number)	# Start BFS from vertex 0
		
		for v in range(self._nvertices):
			if self._vertex_list[v].state == INITIAL:
				component_number += 1
				self._bfs(v, component_number)
		
		print("Number of connected components =", component_number)
		
		if component_number == 1:
			print("Graph is connected")
		else:
			print("Graph is not connected")
			for v in range(self._nvertices):
				print(self._vertex_list[v].name + " -> Component Number :", self._vertex_list[v].component_number)

if __name__ == '__main__':
	
	u_graph = UndirectedGraph()
	
	try:
		# Creating the graph, inserting the vertices and edges
		# Connected Graph
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

		# u_graph.insert_edge("0","1")
		# u_graph.insert_edge("0","3")
		# u_graph.insert_edge("1","2")
		# u_graph.insert_edge("1","4")
		# u_graph.insert_edge("1","5")
		# u_graph.insert_edge("2","3")
		# u_graph.insert_edge("2","5")
		# u_graph.insert_edge("3","6")
		# u_graph.insert_edge("4","7")
		# u_graph.insert_edge("5","6")
		# u_graph.insert_edge("5","7")
		# u_graph.insert_edge("5","8")
		# u_graph.insert_edge("6","9")
		# u_graph.insert_edge("7","8")
		# u_graph.insert_edge("8","9")

		# Not Connected Graph
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
		u_graph.insert_edge("0","3")
		u_graph.insert_edge("1","2")
		u_graph.insert_edge("2","3")

		u_graph.insert_edge("4","5")
		u_graph.insert_edge("4","7")
		u_graph.insert_edge("4","8")
		u_graph.insert_edge("5","6")
		u_graph.insert_edge("5","8")
		u_graph.insert_edge("6","9")
		u_graph.insert_edge("7","8")
		u_graph.insert_edge("8","9")

		u_graph.insert_edge("10","11")
		u_graph.insert_edge("10","13")
		u_graph.insert_edge("10","14")
		u_graph.insert_edge("11","12")
		u_graph.insert_edge("12","13")
		u_graph.insert_edge("13","14")
		
		# Display the graph
		u_graph.display()
		print()
		
		# Find the connected components of graph
		u_graph.connected_component()
		
	except Exception as e:
		print(e)
		
