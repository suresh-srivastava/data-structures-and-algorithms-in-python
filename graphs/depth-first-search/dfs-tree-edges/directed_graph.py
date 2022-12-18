# Copyright (C) Suresh Kumar Srivastava - All Rights Reserved
# DSA Masterclass courses are available on CourseGalaxy.com

# directed_graph.py : Program for traversing a directed graph through DFS and finding the tree edges.

from queue import LifoQueue

INITIAL = 0
VISITED = 1
NIL = -1

class Vertex:
	def __init__(self, name):
		self.name = name
		self.state = None
		self.predecessor = None

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

	def _dfs(self, vertex):
		dfs_stack = LifoQueue()
		
		# Push the start vertex into stack
		dfs_stack.put(vertex)
		
		while dfs_stack.qsize() != 0:
			vertex = dfs_stack.get()
			
			if self._vertex_list[vertex].state == INITIAL:
				self._vertex_list[vertex].state = VISITED

			# Looking for the adjacent vertices of the popped element, and from these push only those vertices into the stack
			# which are in the INITIAL state.
			for i in range(self._nvertices-1,-1,-1):
				# Checking for adjacent vertices with INITIAL state
				if self._is_adjacent(vertex,i) and self._vertex_list[i].state==INITIAL:
					dfs_stack.put(i)
					self._vertex_list[i].predecessor = vertex
		print()

	def dfs_traversal_all(self, vertex_name):
		# Initially all the vertices will have INITIAL state
		for i in range(self._nvertices):
			self._vertex_list[i].state = INITIAL
			self._vertex_list[i].predecessor = NIL

		self._dfs(self._get_index(vertex_name))
		
		for v in range(self._nvertices):
			if self._vertex_list[v].state == INITIAL:
				self._dfs(v)

	def dfs_tree_edges(self, vertex_name):
		self.dfs_traversal_all(vertex_name)
		
		for v in range(self._nvertices):
			p = self._vertex_list[v].predecessor
			if self._vertex_list[v].predecessor != -1:
				print("Vertex :", self._vertex_list[v].name, ", Predecessor :", self._vertex_list[p].name)
			else:
				print("Vertex :", self._vertex_list[v].name, ", Predecessor :", self._vertex_list[v].predecessor)
		
		for v in range(self._nvertices):
			u = self._vertex_list[v].predecessor
			if self._vertex_list[v].predecessor != -1:
				print("Tree Edge - (" + self._vertex_list[u].name + "," + self._vertex_list[v].name + ")")

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
		d_graph.insert_vertex("9")

		d_graph.insert_edge("0","1")
		d_graph.insert_edge("0","3")
		d_graph.insert_edge("1","2")
		d_graph.insert_edge("1","4")
		d_graph.insert_edge("1","5")
		d_graph.insert_edge("2","3")
		d_graph.insert_edge("2","5")
		d_graph.insert_edge("3","6")
		d_graph.insert_edge("4","7")
		d_graph.insert_edge("5","6")
		d_graph.insert_edge("5","7")
		d_graph.insert_edge("5","8")
		d_graph.insert_edge("6","9")
		d_graph.insert_edge("7","8")
		d_graph.insert_edge("8","9")
		
		# Display the graph
		d_graph.display()
		print()
		
		# DFS traversal visiting all the vertices and finding the tree edges
		d_graph.dfs_tree_edges("0")
		
	except Exception as e:
		print(e)
		
