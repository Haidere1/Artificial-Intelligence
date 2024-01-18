graph = {'Abbottabad': set(['Mansehra','Haripur','Muree']),
            'Mansehra':set(['Abbottabad','Attar Shisha','Besham']),
            'Haripur': set(['Hassan Abdal', 'Swabi']),
            'Muree': set(['Islamabad','Muzzafar Abad']),
            'Attar Shisha':set(['Mansehra', 'Naran','Muzzafar Abad']),
            'Besham':set(['Khwazakhela','Chilas']),
            'Hassan Abdal': set(['Jehangira','Taxila']),
            'Swabi':set(['Haripur','Jehangira']),
            'Islamabad':set(['Muree','Rawalpindi']),
            'Muzzafar Abad': set(['Muree','Attar Shisha']),
            'Khwazakhela':set(['Besham','Mingora','Kalam']),
            'Chilas':set(['Besham','Naran','Gilgit']),
            'Jehangira':set(['Swabi','Hassan Abdal','Nowshera']),
            'Taxila':set(['Hassan Abdal','Rawalpindi']),
            'Rawalpindi':set(['Islamabad','Taxila']),
            'Mingora':set(['Nowshera','Khwazakhela']),
            'Kalam':set(['Khwazakhela']),
            'Naran':set(['Attar Shisha','Chilas']),
            'Gilgit':set(['Chilas']),
            'Nowshera':set(['Peshawar','Jehangira']),
            'Peshawar' :set(['Nowshera'])

           }


from collections import deque

class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = set()

    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph_dict[vertex1].add(vertex2)
        self.graph_dict[vertex2].add(vertex1)

    def get_neighbors(self, vertex):
        return self.graph_dict.get(vertex, set())

class BFSPathFinder:
    def __init__(self, graph):
        self.graph = graph

    def find_path(self, start_node, goal_node):
        if start_node not in self.graph.graph_dict or goal_node not in self.graph.graph_dict:
            return None  # Start or goal node is not in the graph

        visited = set()
        queue = deque()
        queue.append([start_node])

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == goal_node:
                return path  # Found a path from start to goal

            if node not in visited:
                neighbors = self.graph.get_neighbors(node)
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

                visited.add(node)

        return None  # No path found from start to goal

# Create an instance of the graph
city_graph = Graph(graph)

# Create an instance of the BFSPathFinder
bfs_path_finder = BFSPathFinder(city_graph)

# Define the start and goal nodes
start_node = 'Abbottabad'
goal_node = 'Peshawar'

# Find the path using BFS
path = bfs_path_finder.find_path(start_node, goal_node)

if path:
    print(f"Path from {start_node} to {goal_node}:")
    print(" -> ".join(path))
else:
    print(f"No path found from {start_node} to {goal_node}.")
