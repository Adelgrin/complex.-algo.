from collections import deque, defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(dict)  # Grafo com capacidade de arestas

    def add_edge(self, u, v, custo):
        self.graph[u][v] = custo
        # Garantir que a aresta reversa exista com capacidade 0
        if v not in self.graph or u not in self.graph[v]:
            self.graph[v][u] = 0

    def bfs(self, s, t, parent):
        visited = set()
        queue = deque([s])
        visited.add(s)

        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if v not in visited and self.graph[u][v] > 0:
                    parent[v] = u
                    visited.add(v)
                    if v == t:
                        return True
                    queue.append(v)
        return False

    def edmonds_karp(self, source, sink):
        parent = {}
        max_flow = 0

        while self.bfs(source, sink, parent):
            # Achar capacidade mínima no caminho encontrado
            path_flow = float('inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Atualizar capacidades do grafo
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

            max_flow += path_flow

        return max_flow


# Exemplo de uso:
if __name__ == "__main__":
    g = Graph(6)  # Número de vértices

    # Adicionando as arestas: g.add_edge(u, v, capacidade)
    g.add_edge(0, 1, 16)
    g.add_edge(0, 2, 13)
    g.add_edge(1, 2, 10)
    g.add_edge(1, 3, 12)
    g.add_edge(2, 1, 4)
    g.add_edge(2, 4, 14)
    g.add_edge(3, 2, 9)
    g.add_edge(3, 5, 20)
    g.add_edge(4, 3, 7)
    g.add_edge(4, 5, 4)

    source = 0
    sink = 5

    print(f"Fluxo máximo é: {g.edmonds_karp(source, sink)}")
