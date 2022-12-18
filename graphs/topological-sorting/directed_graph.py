# Copyright (C) Suresh Kumar Srivastava - All Rights Reserved
# DSA Masterclass courses are available on CourseGalaxy.com

# directed_graph.py : Program for topological sorting of directed acyclic graph.

from queue import Queue

class Vertex:
	def __init__(self, name):
		self.name = name

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

	def _get_indegree(self, vertex):	
		indegree = 0
		for v in range(self._nvertices):
			if self._adj[v][vertex] != 0:
				indegree += 1
		
		return indegree

	def topological_order(self):
		topo_order = []
		indegree = []
		q = Queue()

		# Get the indegree of each vertex
		for v in range(self._nvertices):
			indegree.append(self._get_indegree(v))
			if indegree[v] == 0:
				q.put(v)

		count = 0
		while q.qsize()>0 and count<self._nvertices:
			v = q.get()
		
			count += 1
			topo_order.append(v)	# Add vertex v to topoOrder array

			# Delete all the edges going from vertex v
			for i in range(self._nvertices):
				if self._adj[v][i] != 0:
					self._adj[v][i] = 0
					indegree[i] = indegree[i]-1
					if indegree[i] == 0:
						q.put(i)
						
		if count < self._nvertices:
			raise Exception("Graph contains cycle. Topological order is not possible.")
			
		print("Vertices in topological order are :")
		for u in topo_order:
			print(self._vertex_list[u].name, end=" ")
		print()

if __name__ == '__main__':
	
	d_graph = DirectedGraph()
	
	try:
		# Creating the graph, inserting the vertices and edges
		# Graph without cycle
		d_graph.insert_vertex("0")
		d_graph.insert_vertex("1")
		d_graph.insert_vertex("2")
		d_graph.insert_vertex("3")
		d_graph.insert_vertex("4")
		d_graph.insert_vertex("5")
		d_graph.insert_vertex("6")

		d_graph.insert_edge("0","1")
		d_graph.insert_edge("0","5")
		d_graph.insert_edge("1","4")
		d_graph.insert_edge("1","5")
		d_graph.insert_edge("2","1")
		d_graph.insert_edge("2","3")
		d_graph.insert_edge("3","1")
		d_graph.insert_edge("3","4")
		d_graph.insert_edge("4","5")
		d_graph.insert_edge("6","4")
		d_graph.insert_edge("6","5")

		# Graph with cycle
		# d_graph.insert_vertex("0")
		# d_graph.insert_vertex("1")
		# d_graph.insert_vertex("2")
		# d_graph.insert_vertex("3")
		# d_graph.insert_vertex("4")

		# d_graph.insert_edge("0","1")
		# d_graph.insert_edge("0","2")
		# d_graph.insert_edge("1","3")
		# d_graph.insert_edge("2","4")
		# d_graph.insert_edge("3","0")
		# d_graph.insert_edge("3","4")
		
		# Display the graph
		d_graph.display()
		print()

		d_graph.topological_order()
		
	except Exception as e:
		print(e)
		
