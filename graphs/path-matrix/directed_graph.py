# Copyright (C) Suresh Kumar Srivastava - All Rights Reserved
# DSA Masterclass courses are available on CourseGalaxy.com

# directed_graph.py : Program to find out the path matrix by powers of adjacency matrix.

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

	def path_matrix(self):
		adjp = [ [None for column in range(self._nvertices)] for row in range(self._nvertices) ]
		x = [ [None for column in range(self._nvertices)] for row in range(self._nvertices) ]
		temp = [ [None for column in range(self._nvertices)] for row in range(self._nvertices) ]
		path = [ [None for column in range(self._nvertices)] for row in range(self._nvertices) ]
	
		# Initialize x
		for i in range(self._nvertices):
			for j in range(self._nvertices):
				x[i][j] = 0
		
		# Initially adjp and x is equal to adj
		for i in range(self._nvertices):
			for j in range(self._nvertices):
				x[i][j] = adjp[i][j] = self._adj[i][j]
		
		# Get the matrix x by adding all the adjp
		for p in range(2, self._nvertices+1):
			# adjp(1...n) x adj
			for i in range(self._nvertices):
				for j in range(self._nvertices):
					temp[i][j] = 0
					for k in range(self._nvertices):
						temp[i][j] = temp[i][j] + adjp[i][k]*self._adj[k][j]
						
			# Now adjp will be equal to temp
			for i in range(self._nvertices):
				for j in range(self._nvertices):
					adjp[i][j] = temp[i][j]
			
			# x = adjp1 + adjp2 + ...... + adjpn
			for i in range(self._nvertices):
				for j in range(self._nvertices):
					x[i][j] = x[i][j] + adjp[i][j]
					
		# Display x
		print("x matrix is :")
		for i in range(self._nvertices):
			for j in range(self._nvertices):
				print(x[i][j], end=" ")
			print()
			
		# Assign values to path matrix
		for i in range(self._nvertices):
			for j in range(self._nvertices):
				if x[i][j] == 0:
					path[i][j] = 0
				else:
					path[i][j] = 1
					
		# Display path matrix
		print("Path matrix is :")
		for i in range(self._nvertices):
			for j in range(self._nvertices):
				print(path[i][j], end=" ")
			print()

if __name__ == '__main__':
	
	d_graph = DirectedGraph()
	
	try:
		# Creating the graph, inserting the vertices and edges
		d_graph.insert_vertex("0")
		d_graph.insert_vertex("1")
		d_graph.insert_vertex("2")
		d_graph.insert_vertex("3")

		d_graph.insert_edge("0","1")
		d_graph.insert_edge("0","3")
		d_graph.insert_edge("1","0")
		d_graph.insert_edge("1","2")
		d_graph.insert_edge("1","3")
		d_graph.insert_edge("2","3")
		d_graph.insert_edge("3","0")
		d_graph.insert_edge("3","2")
		
		# Display the graph
		d_graph.display()
		print()
		
		print("Find the path matrix :");
		d_graph.path_matrix()
		
	except Exception as e:
		print(e)
		
