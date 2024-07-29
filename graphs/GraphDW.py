#Directed and weighted graph implementation
class GraphDW:
    def __init__(self, size):
        self.adj_matrix= [[None] * 3 for _ in range(size)]
        self.size= size
        self.vertex_data= [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v]= weight

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex]= data

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(''.join(map()))