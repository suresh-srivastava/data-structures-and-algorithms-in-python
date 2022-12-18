# Copyright (C) Suresh Kumar Srivastava - All Rights Reserved
# DSA Masterclass courses are available on CourseGalaxy.com

# directed_weighted_graph.py : Program to find shortest paths using Bellman Ford algorithm.

from queue import Queue

INFINITY = 9999
NIL = -1

class Vertex:
	def __init__(self, name):
		self.name = name
		self.predecessor = None
		self.path_length = None
		self.in_queue = None

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

	def _bellman_ford_algorithm(self, s):
		qu = Queue()
		current = None
		k = 0
		
		# Make all vertices temporary
		for i in range(self._nvertices):
			self._vertex_list[i].predecessor = NIL
			self._vertex_list[i].path_length = INFINITY
			self._vertex_list[i].in_queue = False

		# Make path_length of source vertex equal to 0
		self._vertex_list[s].path_length = 0
		qu.put(s)
		self._vertex_list[s].in_queue = True
		
		while qu.qsize() != 0:
			# Search for temporary vertex with minimum pathLength and make it current vertex
			current = qu.get()
			self._vertex_list[current].in_queue = False

			if s == current:
				k += 1
			
			if k > self._nvertices:	# Negative cycle reachable from source vertex
				raise Exception("There is negative cycle in graph.")

			for v in range(self._nvertices):
				# Checks for adjacent temporary vertices
				if self._is_adjacent(current,v):
					if (self._vertex_list[current].path_length + self._adj[current][v]) < self._vertex_list[v].path_length:
						self._vertex_list[v].predecessor = current	# Relabel
						self._vertex_list[v].path_length = self._vertex_list[current].path_length + self._adj[current][v]
						if self._vertex_list[v].in_queue == False:
							qu.put(v)
							self._vertex_list[v].in_queue = True

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
		
		self._bellman_ford_algorithm(s)

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
		dw_graph.insert_edge("0","2",9)
		dw_graph.insert_edge("0","4",7)
		dw_graph.insert_edge("1","5",9)
		dw_graph.insert_edge("2","0",5)
		dw_graph.insert_edge("2","1",-4)
		dw_graph.insert_edge("2","3",3)
		dw_graph.insert_edge("3","1",3)
		dw_graph.insert_edge("3","2",6)
		dw_graph.insert_edge("3","5",4)
		dw_graph.insert_edge("4","7",16)
		dw_graph.insert_edge("5","0",4)
		dw_graph.insert_edge("5","6",-8)
		dw_graph.insert_edge("5","7",5)
		dw_graph.insert_edge("6","3",5)
		dw_graph.insert_edge("6","7",2)

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
		
