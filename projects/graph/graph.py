"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # TODO
        # create new key with vertex ID
        # set the value to an empty set - no edges
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set() 
        
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # TODO
        # find vertex v1 in vertices and add vertex v2 to set of edges
        if v1 in self.vertices and v2 in self.vertices: 
            self.vertices[v1].add(v2)
        else:
            raise ValueError('vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # TODO
        if vertex_id in self.vertices:  
            return self.vertices[vertex_id]
        else: 
            raise ValueError('vertex does not exist')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # TODO
        # create a queue  
        q = Queue()
        # enqueue the staring vertex
        q.enqueue(starting_vertex)
        # create a set to store visited vertices
        visited = set()
        # while queue is not empty, dequeue the first vertex
        while q.size() > 0:
            v = q.dequeue()
            # check if vertex has not been visited, mark visited
            if v not in visited:
                print(v)
                visited.add(v)
                # enqueue all the neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # TODO
        # create a stack  
        s = Stack()
        # push the starting vertex
        s.push(starting_vertex)
        # create a set to store visited vertices
        visited = set()
        # while the stack is not empty, pop the first vertex
        while s.size() > 0:
            v = s.pop()
            # check if vertex has not been visted, mark visited
            if v not in visited:
                print(v)
                visited.add(v)
                # push the neighbors onto the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # TODO
        if visited is None:
            visited = set()
        # check if the node has been visited, mark visited
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            # call dft_recursive on each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

        # def dft_recursive(self, starting_vertex):
        # visited = set()
        # def dft(vertex):
        #     if vertex in visited:
        #         return 
        #     else:
        #         visited.add(vertex)
        #         print(vertex)
        #     for neighbor in self.get_neighbors(vertex):
        #         dft(neighbor)
        # dft(starting_vertex)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # TODO
        # create a queue  
        q = Queue()
        # enqueue a path to the starting vertex
        q.enqueue([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while the queue in not empty, dequeue the first path
        while q.size() > 0:
            path = q.dequeue()
            # grab the vertex from the end of the path
            v = path [-1]
            # check if vertex has been visited, mark visited
            if v not in visited:
                visited.add(v)
                # check if it is the target, return path if it is
                if v == destination_vertex:
                    return path
                # enqueue path and the neighbors
                for neighbor in self.get_neighbors(v):
                    # make a copy of the path
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    # enqueue the path copy
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # TODO
        # create a stack  
        s = Stack()
        # push the starting vertex
        s.push([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while the stack in not empty, pop the first path
        while s.size() > 0:
            path = s.pop()
            # grab the vertex from the end of the path
            v = path [-1]
            # check if vertex has been visited, mark visited
            if v not in visited:
                visited.add(v)
                # check if it is the target, return path if it is
                if v == destination_vertex:
                    return path
                # push path and the neighbors
                for neighbor in self.get_neighbors(v):
                    # make a copy of the path
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    # push the path coppy
                    s.push(path_copy)

    # def dfs_recursive(self, starting_vertex, destination_vertex):
    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # TODO
        if visited is None:
            visited = set()
        if path is None:
            path = []
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            if starting_vertex == destination_vertex:
                return path_copy
            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path_copy)
                if new_path is not None:
                    return new_path
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
