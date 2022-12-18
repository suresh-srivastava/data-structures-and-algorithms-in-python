# Copyright (C) Suresh Kumar Srivastava - All Rights Reserved
# DSA Masterclass courses are available on CourseGalaxy.com

# undirected_graph.py : Program for traversing an undirected graph through DFS using recursion and finding out that graph is 
# cyclic or not

INITIAL = 0
VISITED = 1
FINISHED = 2

class Vertex:
	def __init__(self, name):
		self.name = name
		self.state = None
		self.predecessor = None

class UndirectedGraph:
	has_cycle = None

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
		self._vertex_list[vertex].state = VISITED

		for i in range(self._nvertices):
			if self._is_adjacent(vertex,i) and self._vertex_list[vertex].predecessor!=i:
				if self._vertex_list[i].state==INITIAL:
					# It's Tree Edge
					self._vertex_list[i].predecessor = vertex
					self._dfs(i)
				elif self._vertex_list[i].state == VISITED:
					# It's Back Edge
					UndirectedGraph.has_cycle = True
		
		self._vertex_list[vertex].state = FINISHED
	
	def is_cyclic(self):
		# Initially all the vertices will have INITIAL state
		for i in range(self._nvertices):
			self._vertex_list[i].state = INITIAL
		
		UndirectedGraph.has_cycle = False
		
		for v in range(self._nvertices):
			if self._vertex_list[v].state == INITIAL:
				self._dfs(v)

		return UndirectedGraph.has_cycle

if __name__ == '__main__':
	
	u_graph = UndirectedGraph()

	try:
		# Creating the graph, inserting the vertices and edges
		# Graph is acyclic
		# u_graph.insert_vertex("0")
		# u_graph.insert_vertex("1")
		# u_graph.insert_vertex("2")
		# u_graph.insert_vertex("3")
		# u_graph.insert_vertex("4")
		# u_graph.insert_vertex("5")

		# u_graph.insert_edge("0","1")
		# u_graph.insert_edge("1","3")
		# u_graph.insert_edge("2","3")
		# u_graph.insert_edge("3","4")
		# u_graph.insert_edge("4","5")

		# Graph is cyclic
		u_graph.insert_vertex("0")
		u_graph.insert_vertex("1")
		u_graph.insert_vertex("2")
		u_graph.insert_vertex("3")
		u_graph.insert_vertex("4")
		u_graph.insert_vertex("5")

		u_graph.insert_edge("0","1")
		u_graph.insert_edge("0","2")
		u_graph.insert_edge("1","3")
		u_graph.insert_edge("2","3")
		u_graph.insert_edge("3","4")
		u_graph.insert_edge("4","5")

		# Display the graph
		u_graph.display()
		print()
		
		if u_graph.is_cyclic():
			print("Graph is Cyclic")
		else:
			print("Graph is Acyclic")

	except Exception as e:
		print(e)
		
