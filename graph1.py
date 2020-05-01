
class Graph:

    #Initialize the graph
    def __init__(self):
        self.vertices = {}
        self.no_of_nodes = 0

    #Function to add egde in the graph           
    def add_edge(self, src, dest, edge_weight):
        if src > 600 or dest > 600:
            return
        if src not in self.vertices:
            self.vertices[src]={}

        if dest not in self.vertices:
            self.vertices[dest] = {}
        if src > self.no_of_nodes:
            self.no_of_nodes = src
        if dest > self.no_of_nodes:
            self.no_of_nodes = dest
        self.vertices[src][dest] = edge_weight

    #function to print the graph
    def print_graph(self):
    	
    	for node in self.vertices:
    		print(node , end = "->")
    		for var in self.vertices[node]:
    			print(var,"(",self.vertices[node][var],")", end =" ")
    		print('\n')  
    		

