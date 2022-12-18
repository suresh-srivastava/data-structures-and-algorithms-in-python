# Copyright (C) Suresh Kumar Srivastava - All Rights Reserved
# DSA Masterclass courses are available on CourseGalaxy.com

# directed_graph_list.py : Program for directed graph using adjacency list.

class VertexNode:
	def __init__(self, name):
		self.name = name
		self.next_vertex = None
		self.first_edge = None

class EdgeNode:
	def __init__(self, v):
		self.end_vertex = v
		self.next_edge = None

class DirectedGraphList:
	def __init__(self):
		self._nvertices = 0
		self._nedges = 0
		self._start = None

	def insert_vertex(self, vertex_name):
		ptr = None
		temp = None
		vertex_found = False

		ptr = self._start
		
		if ptr == None:
			temp = VertexNode(vertex_name)
			self._start = temp
			self._nvertices += 1
		else:
			while ptr.next_vertex != None:
				if ptr.name == vertex_name:
					vertex_found = True
					break
				ptr = ptr.next_vertex
				
			if vertex_found or ptr.name==vertex_name:
				print("Vertex already present")
			else:
				temp = VertexNode(vertex_name)
				ptr.next_vertex = temp
				self._nvertices += 1
				
	def _find_vertex(self, vertex_name):
		ptr = self._start

		while ptr != None:
			if ptr.name == vertex_name:
				break
			
			ptr = ptr.next_vertex
			
		return ptr
	
	def insert_edge(self, source, destination):
		u = None
		v = None
		edge_ptr = None
		temp = None
		
		edge_found = False
		
		if source == destination:
			print("Invalid Edge : source and destination vertices are same")
		else:
			u = self._find_vertex(source)
			v = self._find_vertex(destination)
			
			if u == None:
				print("Source vertex not present, first insert vertex " + source)
			elif v == None:
				print("Destination vertex not present, first insert vertex " + destination)
			else:
				if u.first_edge == None:
					temp = EdgeNode(v)
					u.first_edge = temp
					self._nedges += 1
				else:
					edge_ptr = u.first_edge
					
					while edge_ptr.next_edge != None:
						if edge_ptr.end_vertex.name == v.name:
							edge_found = True
							break
						
						edge_ptr = edge_ptr.next_edge
						
					if edge_found or edge_ptr.end_vertex.name==destination:
						print("Edge already present")
					else:
						temp = EdgeNode(v)
						edge_ptr.next_edge = temp
						self._nedges += 1
					
	def delete_vertex(self, vertex_name):
		self._delete_from_edge_lists(vertex_name)
		self._delete_from_vertex_list(vertex_name)
	
	# Delete incoming edges
	def _delete_from_edge_lists(self, vertex_name):
		vertex_ptr = None
		edge_ptr = None
		
		vertex_ptr = self._start
		
		while vertex_ptr != None:
			if vertex_ptr.first_edge != None:
				if vertex_ptr.first_edge.end_vertex.name == vertex_name:
					vertex_ptr.first_edge = vertex_ptr.first_edge.next_edge
					self._nedges -= 1
					continue
				
				edge_ptr = vertex_ptr.first_edge
				while edge_ptr.next_edge != None:
					if edge_ptr.next_edge.end_vertex.name == vertex_name:
						edge_ptr.next_edge = edge_ptr.next_edge.next_edge
						self._nedges -= 1
						continue
					edge_ptr = edge_ptr.next_edge

			vertex_ptr = vertex_ptr.next_vertex
			
	# Delete outgoing edges and vertex
	def _delete_from_vertex_list(self, vertex_name):
		vertex_ptr = None
		temp_vertex = None
		edge_ptr = None
		
		if self._start == None:
			print("No vertices to be deleted")
			return
			
		if self._start.name == vertex_name:
			temp_vertex = self._start
			self._start = self._start.next_vertex
		else:	# vertex to be deleted is in between or at last
			vertex_ptr = self._start
			while vertex_ptr.next_vertex != None:
				if vertex_ptr.next_vertex.name == vertex_name:
					break
				vertex_ptr = vertex_ptr.next_vertex
				
			if vertex_ptr.next_vertex != None:
				temp_vertex = vertex_ptr.next_vertex
				vertex_ptr.next_vertex = vertex_ptr.next_vertex.next_vertex
			else:
				print("Vertex not found")
				
		if temp_vertex != None:
			edge_ptr = temp_vertex.first_edge
			while edge_ptr != None:
				edge_ptr = edge_ptr.next_edge
				self._nedges -= 1
			self._nvertices -= 1
			
	def delete_edge(self, source, destination):
		vertex_ptr = None
		edge_ptr = None
		
		vertex_ptr = self._find_vertex(source)
		
		if vertex_ptr == None:
			print("Edge not found")
		else:
			edge_ptr = vertex_ptr.first_edge
			
			if edge_ptr == None:
				print("Edge not found")
			else:
				if edge_ptr.end_vertex.name == destination:
					vertex_ptr.first_edge = edge_ptr.next_edge
					self._nedges -= 1
				else:
					while edge_ptr.next_edge != None:
						if edge_ptr.next_edge.end_vertex.name == destination:
							break
						edge_ptr = edge_ptr.next_edge
					
					if edge_ptr.next_edge == None:
						print("Edge not found")
					else:
						edge_ptr.next_edge = edge_ptr.next_edge.next_edge
						self._nedges -= 1
						
	def display(self):
		vertex_ptr = None
		edge_ptr = None
		
		vertex_ptr = self._start
		
		while vertex_ptr != None:
			print("Vertex : " + vertex_ptr.name)
			
			edge_ptr = vertex_ptr.first_edge
			while edge_ptr != None:
				print("Edge : " + vertex_ptr.name + " -> " + edge_ptr.end_vertex.name)
				edge_ptr = edge_ptr.next_edge
				
			vertex_ptr = vertex_ptr.next_vertex
			
	def edge_exists(self, source, destination):
		vertex_ptr = None
		edge_ptr = None
		edge_found = False
		
		vertex_ptr = self._find_vertex(source)
		
		if vertex_ptr != None:
			edge_ptr = vertex_ptr.first_edge
			while edge_ptr != None:
				if edge_ptr.end_vertex.name == destination:
					edge_found = True
					break
				edge_ptr = edge_ptr.next_edge
				
		return edge_found
		
	def get_outdegree(self, vertex):
		vertex_ptr = None
		edge_ptr = None
		outdegree = 0
		
		vertex_ptr = self._find_vertex(vertex)
		if vertex_ptr == None:
			raise Exception("Invalid Vertex")
		
		edge_ptr = vertex_ptr.first_edge
		while edge_ptr != None:
			outdegree += 1
			edge_ptr = edge_ptr.next_edge
			
		return outdegree
		
	def get_indegree(self, vertex):
		vertex_ptr = None
		edge_ptr = None
		indegree = 0
	
		if self._find_vertex(vertex) == None:
			raise Exception("Invalid Vertex")
		
		vertex_ptr = self._start
		while vertex_ptr != None:
			edge_ptr = vertex_ptr.first_edge
			while edge_ptr != None:
				if edge_ptr.end_vertex.name == vertex:
					indegree += 1
				edge_ptr = edge_ptr.next_edge
			vertex_ptr = vertex_ptr.next_vertex
			
		return indegree
	
if __name__ == '__main__':
	
	d_graph = DirectedGraphList()
	
	try:
		# Creating the graph, inserting the vertices and edges
		d_graph.insert_vertex("0")
		d_graph.insert_vertex("1")
		d_graph.insert_vertex("2")
		d_graph.insert_vertex("3")

		d_graph.insert_edge("0","3")
		d_graph.insert_edge("1","2")
		d_graph.insert_edge("2","3")
		d_graph.insert_edge("3","1")
		d_graph.insert_edge("0","2")
		
		# Display the graph
		d_graph.display()
		print()
		
		# Deleting an edge
		d_graph.delete_edge("0","2")
			
		# Display the graph
		d_graph.display()
		print()

		# Deleting a vertex
		d_graph.delete_vertex("0")

		# Display the graph
		d_graph.display()
		print()
		
		# Check if there is an edge between two vertices
		print("Edge exist : ", d_graph.edge_exists("2","3"))
		
		# Display Outdegree and Indegree of a vertex
		print("Outdegree : ", d_graph.get_outdegree("3"))
		print("Indegree : ", d_graph.get_indegree("3"))
		
	except Exception as e:
		print(e)	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

		
