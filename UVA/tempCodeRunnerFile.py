from collections import defaultdict, deque

class Graph:
  def __init__(self):
    self.graph = defaultdict(list)
  def add_edge(self, node, neighbour):
    self.graph[node].append(neighbour)


g = Graph()
g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('B','A')
g.add_edge('A','D')
g.add_edge('A','E')
g.add_edge('C','A')
g.add_edge('C','F')
g.add_edge('D','B')
g.add_edge('E','B')
g.add_edge('E','F')
g.add_edge('F','C')
g.add_edge('F','E')


def bfs(graph, root):
    visited = set()
    queue = deque([root])

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        # if vertex == search_value:
        #     return True
        visited.add(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
    # return False

bfs(g.graph, "F")