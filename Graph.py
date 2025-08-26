from queue import Queue

class Graph:
    def __init__(self, V=None, E=None):
        raise NotImplementedError("Graph is an abstract base class.")

    def is_connected(self, v1, v2):
        visited = set()
        q = Queue()
        q.put(v1)
        visited.add(v1)
        while not q.empty():
            v = q.get()
            if v == v2:
                return True
            for nbr in self.nbrs(v):
                if nbr not in visited:
                    visited.add(nbr)
                    q.put(nbr)
        return False

    def bfs(self, v):
        tree = {v: None}
        visited = set([v])
        q = Queue()
        q.put(v)
        while not q.empty():
            current = q.get()
            for nbr in self.nbrs(current):
                if nbr not in visited:
                    visited.add(nbr)
                    tree[nbr] = current
                    q.put(nbr)
        return tree

    def shortest_path(self, v1, v2):
        tree = self.bfs(v1)
        if v2 not in tree:
            return []
        path = []
        current = v2
        while current is not None:
            path.append(current)
            current = tree[current]
        return list(reversed(path))

    def count_trees(self):
        visited = set()
        trees = []
        for v in self:
            if v not in visited:
                tree = self.bfs(v)
                trees.append(tree)
                visited.update(tree.keys())
        return trees, len(trees)


class AdjacencySetGraph(Graph):
    def __init__(self, V=None, E=None):
        self._adj = dict()
        if V:
            for v in V:
                self.add_vertex(v)
        if E:
            for e in E:
                self.add_edge(e)

    def __iter__(self):
        return iter(self._adj)

    def add_vertex(self, v):
        if v not in self._adj:
            self._adj[v] = set()

    def add_edge(self, e):
        a, b = e
        self.add_vertex(a)
        self.add_vertex(b)
        self._adj[a].add(b)
        self._adj[b].add(a)

    def nbrs(self, v):
        return iter(self._adj[v])


class EdgeSetGraph(Graph):
    def __init__(self, V=None, E=None):
        self._verts = set()
        self._edges = set()
        if V:
            self._verts.update(V)
        if E:
            for e in E:
                self.add_edge(e)

    def __iter__(self):
        return iter(self._verts)

    def add_vertex(self, v):
        self._verts.add(v)

    def add_edge(self, e):
        a, b = e
        self.add_vertex(a)
        self.add_vertex(b)
        self._edges.add(tuple(sorted((a, b))))

    def nbrs(self, v):
        return iter({b if a == v else a for (a, b) in self._edges if v in (a, b)})