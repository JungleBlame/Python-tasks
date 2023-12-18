import abc # abstract base class, includes functions that have dfault implementations

import numpy as np # provides number of tools to simplify working with arrays

class Graph(abc.ABC):

    def __init__(self, num_vertices, directed= False):
        self.num_verticies = num_vertices
        self.directed = directed

    @abc.abstractmethod #<-decorator used to ensure each class implements abstract method to be created
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod #<-decorator used to ensure each class implements abstract method to be created
    def remove_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod #<-decorator used to ensure each class implements abstract method to be created
    def get_adjacent_vertices (self, v):
        pass

    @abc.abstractmethod #<-decorator used to ensure each class implements abstract method to be created
    def is_adjacent(self, v1, v2):
        pass

    @abc.abstractmethod #<-decorator used to ensure each class implements abstract method to be created
    def get_indegree(self, v):
        pass
    
    @abc.abstractmethod #<-decorator used to ensure each class implements abstract method to be created
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod #<-decorator used to ensure each class implements abstract method to be created
    def show(self):
        pass

class Vertex:

    def __init__(self, id):
        self.id=id
        self.adjacency_set = set() #or linked list

    def add_edge(self,v):
        if self.id ==v:
            raise ValueError("The vertex %d cannot be adjacent to itself" %v)
        
        self.adjacency_set.add(v)

    def remove_edge(self,v):
        if self.id ==v:
            raise ValueError("The vertex %d cannot be adjacent to itself" %v)
        
        self.adjacency_set.remove(v)

    def get_adjacenet_vertices(self):
        return sorted(self.adjacency_set)
    
    def is_adjacent(self,v):
        return v in self.adjacency_set

class AdjacencySetGraph(Graph):

    def __init__(self, num_vertices, directed=False):

        super(AdjacencySetGraph, self).__init__(num_vertices, directed)

        self.vertex_list=[]
        for i in range(num_vertices):
            v = Vertex(i)

            self.vertex_list.append(v)

    def add_edge (self, v1, v2, weight=1):
        if v1 >= self.num_verticies or v2 >= self.num_verticies or v1 < 0 or v2<0:
            raise ValueError("Verticies %d and %d are out of bounds" % (v1,v2))
        
        if weight != 1:
            raise ValueError ("An adjacency set cannot represent edge weights >1")
        
        self.vertex_list[v1].add_edge(v2)

        if self.directed ==False:
            self.vertex_list[v2.add_edge(v1)]

    def remove_edge(self,v1,v2):
        if v1 >= self.num_verticies or v2 >= self.num_verticies or v1 <0 or v2< 0:
            raise ValueError("Vericies %d and %d are out of bounds" %(v1,v2))
        
        self.vertex_list[v1].remove_edge(v2)

        if self.directed ==False:
            self.vertex_list[v2].remove_edge(v1)
    
    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.num_verticies:
            raise ValueError("Cannot access vertex %d" % v)
        
        return self.vertex_list[v].get_adjacenet_vertices()
    
    def is_adjacent(self, v1, v2):
        if v1>= self.num_verticies or v2 >= self.num_verticies or v1 <0 or v2 <0:
            raise ValueError ("Vertices %d and %d are out of bounds" % (v1,v2))
        
        return self.vertex_list[v1].is_adjacent(v2) or self.vertex_list[v2].is_adjacent(v1)
    
    def get_indegree(self, v):
        if v <0 or v>= self.num_verticies:
            raise ValueError("Cannot access vertex %d" % v)
        
        indegree = 0
        for i in range(self.num_verticies):
            if i ==v:
                continue
            if v in self.get_adjacent_vertices(i):
                indegree= indegree +1
        return indegree
    
    def get_edge_weight(self, v1, v2):
        return 1
    
    def show(self):
        for i in range(self.num_verticies):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)

    
