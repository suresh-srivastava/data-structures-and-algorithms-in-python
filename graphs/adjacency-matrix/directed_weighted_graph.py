# Copyright (C) Suresh Kumar Srivastava - All Rights Reserved
# DSA Masterclass courses are available on CourseGalaxy.com

# directed_weighted_graph.py : Program for directed graph with weight on edge using adjacency matrix.

class Vertex:
	def __init__(self, name):
		self.name = name

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
			
	def delete_edge(self, source, destination):
		u = self._get_index(source)
		v = self._get_index(destination)
		
		if self._adj[u][v] != 0:
			self._adj[u][v] = 0
			self._nedges -= 1
		else:
			print("Edge doesn't exist")
			
	def display(self):
		for i in range(self._nvertices):
			for j in range(self._nvertices):
				print(self._adj[i][j], end=" ")
			print()

	def _is_adjacent(self, u, v):
		return self._adj[u][v] != 0
		
	def edge_exists(self, source, destination):
		return self._is_adjacent(self._get_index(source), self._get_index(destination))

	def get_outdegree(self, vertex):
		u = self._get_index(vertex)
		
		outdegree = 0
		for v in range(self._nvertices):
			if self._adj[u][v] != 0:
				outdegree += 1
		
		return outdegree
		
	def get_indegree(self, vertex):
		u = self._get_index(vertex)
		
		indegree = 0
		for v in range(self._nvertices):
			if self._adj[v][u] != 0:
				indegree += 1
		
		return indegree
		
if __name__ == '__main__':
	
	dw_graph = DirectedWeightedGraph()
	
	try:
		# Creating the graph, inserting the vertices and edges
		dw_graph.insert_vertex("0")
		dw_graph.insert_vertex("1")
		dw_graph.insert_vertex("2")
		dw_graph.insert_vertex("3")

		dw_graph.insert_edge("0","3",1)
		dw_graph.insert_edge("1","2",2)
		dw_graph.insert_edge("2","3",3)
		dw_graph.insert_edge("3","1",4)
		dw_graph.insert_edge("0","2",5)
		
		# Display the graph
		dw_graph.display()
		print()
		
		# Deleting an edge
		dw_graph.delete_edge("0","2")
			
		# Display the graph
		dw_graph.display()
		print()

		# Check if there is an edge between two vertices
		print("Edge exist : ", dw_graph.edge_exists("2","3"))
		
		# Display Outdegree and Indegree of a vertex
		print("Outdegree : ", dw_graph.get_outdegree("3"))
		print("Indegree : ", dw_graph.get_indegree("3"))
		
	except Exception as e:
		print(e)
		
