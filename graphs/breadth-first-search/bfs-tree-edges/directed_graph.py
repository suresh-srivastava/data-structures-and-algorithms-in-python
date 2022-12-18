# Copyright (C) Suresh Kumar Srivastava - All Rights Reserved
# DSA Masterclass courses are available on CourseGalaxy.com

# directed_graph.py : Program for traversing a directed graph through BFS and finding the tree edges.

from queue import Queue

INITIAL = 0
WAITING = 1
VISITED = 2

class Vertex:
	def __init__(self, name):
		self.name = name
		self.state = None

class DirectedGraph:
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

	def _bfs(self, vertex):
		bfs_queue = Queue()
		
		# Inserting the start vertex into queue and changing its state to WAITING
		bfs_queue.put(vertex)
		self._vertex_list[vertex].state = WAITING
		
		while bfs_queue.qsize() != 0:
			# Deleting front element from the queue and changing its state to VISITED
			vertex = bfs_queue.get()
			self._vertex_list[vertex].state = VISITED
	
			# Looking for the adjacent vertices of the deleted element, and from these insert only those vertices into the
			# queue which are in the INITIAL state. Change the state of all these inserted vertices from INITIAL to WAITING
			for i in range(self._nvertices):
				# Checking for adjacent vertices with INITIAL state
				if self._is_adjacent(vertex,i) and self._vertex_list[i].state==INITIAL:
					bfs_queue.put(i)
					self._vertex_list[i].state = WAITING
					print("Tree Edge - (" + self._vertex_list[vertex].name + "," + self._vertex_list[i].name + ")")
		print()

	def bfs_traversal_all(self, vertex_name):
		# Initially all the vertices will have INITIAL state
		for i in range(self._nvertices):
			self._vertex_list[i].state = INITIAL
			
		self._bfs(self._get_index(vertex_name))	
		
		for v in range(self._nvertices):
			if self._vertex_list[v].state == INITIAL:
				self._bfs(v)

	def bfs_tree_edges(self, vertex_name):
		self.bfs_traversal_all(vertex_name)

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
		d_graph.insert_edge("0","4")
		d_graph.insert_edge("1","2")
		d_graph.insert_edge("1","4")
		d_graph.insert_edge("2","5")
		d_graph.insert_edge("3","4")
		d_graph.insert_edge("3","6")
		d_graph.insert_edge("4","5")
		d_graph.insert_edge("4","7")
		d_graph.insert_edge("6","4")
		d_graph.insert_edge("6","7")
		d_graph.insert_edge("7","5")
		d_graph.insert_edge("7","8")

		# Display the graph
		d_graph.display()
		print()

		# BFS traversal visiting all the vertices and finding the tree edges
		d_graph.bfs_tree_edges("0")

	except Exception as e:
		print(e)
		
