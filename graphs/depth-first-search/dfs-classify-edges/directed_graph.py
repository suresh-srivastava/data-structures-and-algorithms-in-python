# Copyright (C) Suresh Kumar Srivastava - All Rights Reserved
# DSA Masterclass courses are available on CourseGalaxy.com

# directed_graph.py : Program for traversing a directed graph through DFS using recursion and classify all the edges in graph.

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
		self._vertex_list[vertex].state = VISITED
		DirectedGraph.time += 1
		self._vertex_list[vertex].discovery_time = DirectedGraph.time	# discovery time

		for i in range(self._nvertices):
			if self._is_adjacent(vertex,i):
				if self._vertex_list[i].state==INITIAL:
					print("Tree Edge - (" + self._vertex_list[vertex].name + "-" + self._vertex_list[i].name + ")")
					self._dfs(i)
				elif self._vertex_list[i].state==VISITED:
					print("Back Edge - (" + self._vertex_list[vertex].name + "-" + self._vertex_list[i].name + ")")
				elif self._vertex_list[vertex].discovery_time < self._vertex_list[i].discovery_time:
					print("Forward Edge - (" + self._vertex_list[vertex].name + "-" + self._vertex_list[i].name + ")")
				else:
					print("Cross Edge - (" + self._vertex_list[vertex].name + "-" + self._vertex_list[i].name + ")")
		
		self._vertex_list[vertex].state = FINISHED
		DirectedGraph.time += 1
		self._vertex_list[vertex].finishing_time = DirectedGraph.time	# finishing time

	def dfs_classify_edges(self):
		# Initially all the vertices will have INITIAL state
		for i in range(self._nvertices):
			self._vertex_list[i].state = INITIAL
		
		DirectedGraph.time = 0
		
		for v in range(self._nvertices):
			if self._vertex_list[v].state == INITIAL:
				self._dfs(v)
		print()

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
		d_graph.insert_vertex("10")
		d_graph.insert_vertex("11")
		d_graph.insert_vertex("12")
		d_graph.insert_vertex("13")
		d_graph.insert_vertex("14")
		d_graph.insert_vertex("15")

		d_graph.insert_edge("0","1")
		d_graph.insert_edge("0","2")
		d_graph.insert_edge("0","3")
		d_graph.insert_edge("1","2")
		d_graph.insert_edge("3","2")
		d_graph.insert_edge("4","1")
		d_graph.insert_edge("4","5")
		d_graph.insert_edge("4","6")
		d_graph.insert_edge("4","7")
		d_graph.insert_edge("5","6")
		d_graph.insert_edge("6","3")
		d_graph.insert_edge("6","9")
		d_graph.insert_edge("7","8")
		d_graph.insert_edge("8","4")
		d_graph.insert_edge("8","5")
		d_graph.insert_edge("8","9")
		d_graph.insert_edge("9","5")
		d_graph.insert_edge("10","11")
		d_graph.insert_edge("10","14")
		d_graph.insert_edge("11","8")
		d_graph.insert_edge("11","12")
		d_graph.insert_edge("11","14")
		d_graph.insert_edge("11","15")
		d_graph.insert_edge("12","15")
		d_graph.insert_edge("13","10")
		d_graph.insert_edge("14","13")
		d_graph.insert_edge("14","15")
		
		# Display the graph
		d_graph.display()
		print()
		
		# classify all the edges in graph
		d_graph.dfs_classify_edges()
		
	except Exception as e:
		print(e)
		
