class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def greedy_coloring(self):
        colors = {}  # Dictionary to store colors for each node
        colored = set()  # Set to track colored nodes

        for node in self.graph:
            used_colors = set()
            for neighbor in self.graph[node]:
                if neighbor in colored:
                    used_colors.add(colors[neighbor])

            # Find the smallest unused color for the current node
            for color in range(len(self.graph)):
                if color not in used_colors:
                    colors[node] = color
                    break

            colored.add(node)

        return colors

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

color_mapping = g.greedy_coloring()
print("Node -> Color")
for node, color in color_mapping.items():
    print(f"{node} -> {color}")
