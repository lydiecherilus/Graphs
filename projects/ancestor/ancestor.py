def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(parent, child)

        longest_path = 1
        earliest_ancestor = -1

    for vertex in graph.vertices:
        path = graph.dfs(vertex, starting_node)

        if path:
            if len(path) > longest_path:
                longest_path = len(path)
                earliest_ancestor = vertex

    return earliest_ancestor


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set() 
        
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices: 
            self.vertices[v1].add(v2)
        else:
            raise ValueError('vertex does not exist')

    def get_neighbors(self, vertex_id):
        if vertex_id in self.vertices:  
            return self.vertices[vertex_id]
        else: 
            raise ValueError('vertex does not exist')

    def dfs(self, starting_vertex, destination_vertex):
        # return a list of path from depth-first order.
        s = Stack()
        s.push([starting_vertex])
        visited = set()
        while s.size() > 0:
            path = s.pop()
            # grab the vertex from the end of the path
            current_node = path [-1]
            # check if vertex has been visited, mark visited
            if current_node not in visited:
                visited.add(current_node)
                # check if it is the target, return path if it is
                if current_node == destination_vertex:
                    return path
                # push path and the neighbors
                for neighbor in self.get_neighbors(current_node):
                    # make a copy of the path
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    s.push(path_copy)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)