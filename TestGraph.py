import unittest
from Graph import Graph, AdjacencySetGraph, EdgeSetGraph

class GraphTestFactory:
    def graph_ds(self, V=None, E=None):
        raise NotImplementedError

    def test_graph_construction(self):
        g = self.graph_ds()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_edge(('A', 'B'))
        self.assertIn('A', list(g))
        self.assertIn('B', list(g))
        self.assertIn('B', list(g.nbrs('A')))
        self.assertIn('A', list(g.nbrs('B')))

    def test_graph_construction_init(self):
        V = {'A', 'B', 'C'}
        E = {('A', 'B'), ('B', 'C')}
        g = self.graph_ds(V, E)
        self.assertIn('A', list(g))
        self.assertIn('B', list(g.nbrs('A')))
        self.assertIn('C', list(g.nbrs('B')))

    def test_is_connected_simple(self):
        V = {'A', 'B', 'C', 'D'}
        E = {('A', 'B'), ('B', 'C')}
        g = self.graph_ds(V, E)
        self.assertTrue(g.is_connected('A', 'C'))
        self.assertFalse(g.is_connected('A', 'D'))

    def test_is_connected_cycle(self):
        V = {'A', 'B', 'C'}
        E = {('A', 'B'), ('B', 'C'), ('C', 'A')}
        g = self.graph_ds(V, E)
        self.assertTrue(g.is_connected('A', 'C'))

    def test_bfs(self):
        V = {'A', 'B', 'C', 'D', 'E'}
        E = {('A', 'B'), ('A', 'C'), ('B', 'D'), ('D', 'E')}
        g = self.graph_ds(V, E)
        tree = g.bfs('A')
        dist_actual = {}
        for v in tree:
            curr = v
            dist = 0
            while tree[curr] is not None:
                curr = tree[curr]
                dist += 1
            dist_actual[v] = dist
        dist_expected = {'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 3}
        self.assertEqual(dist_actual, dist_expected)

    def test_count_trees(self):
        V = {'A', 'B', 'C', 'D', 'E'}
        E = {('A', 'B'), ('B', 'C'), ('D', 'E')}
        g = self.graph_ds(V, E)
        trees, count = g.count_trees()
        tree_vertices = [set(t.keys()) for t in trees]
        self.assertEqual(count, 2)
        self.assertIn(set(['A', 'B', 'C']), tree_vertices)
        self.assertIn(set(['D', 'E']), tree_vertices)

    def test_shortest_path(self):
        V = {'A', 'B', 'C', 'D', 'E'}
        E = {('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')}
        g = self.graph_ds(V, E)
        path = g.shortest_path('A', 'E')
        for i in range(len(path) - 1):
            edge = (path[i], path[i+1])
            reverse_edge = (path[i+1], path[i])
            self.assertTrue(edge in E or reverse_edge in E)
        self.assertEqual(len(path) - 1, 4)

class TestAdjacency(GraphTestFactory, unittest.TestCase):
    def graph_ds(self, V=None, E=None):
        return AdjacencySetGraph(V, E)

class TestEdge(GraphTestFactory, unittest.TestCase):
    def graph_ds(self, V=None, E=None):
        return EdgeSetGraph(V, E)

class TestGraphAbstract(unittest.TestCase):
    def test_graph_init_raises(self):
        with self.assertRaises(NotImplementedError):
            Graph()

unittest.main()