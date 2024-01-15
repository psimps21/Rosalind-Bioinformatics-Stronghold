import numpy as np
import sys

"""
Given: A positive integer n (n≤1000) and an adjacency list corresponding to a graph on n
 nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce a tree.

This problem can be solved by identifying the number of connected components in the graph
"""
class UndirectedGraph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.edges = edges

        # define Adjecency list
        self.adj_map = {i+1:set() for i in range(num_nodes)}

        # populate adjcency list
        for pair in edges:
            u,v = pair
            self.adj_map[u].add(v)
            self.adj_map[v].add(u)

    def num_nodes(self):
        return self.num_nodes
    
    def num_edges(self):
        return sum([len(x) for x in self.adj_map.values()]) / 2
    
    def CompleteATree(self):
        cc_map = {i+1:set([i+1]) for i in range(self.num_nodes)}

        for pair in self.edges:
            u,v = pair
            new_cc = cc_map[u].union(cc_map[v])

            for e in new_cc:
                cc_map[e] = new_cc

        connected_components = set(frozenset(s) for k,s in cc_map.items())
        # print('Connected components:', *connected_components)

        return len(connected_components) - 1
    
    def PrimMST(self):
        mst_edges = []

        # Select a random start node
        start_node = np.random.randint(1,1+self.num_nodes)
        print('Start node:', start_node)

        nodes_in_tree = set([start_node])
        nodes_not_in_tree = set(range(1,1+self.num_nodes))
        nodes_not_in_tree.remove(start_node)
        print('Nodes in tree:', *nodes_in_tree)
        print('Nodes not in tree:', *nodes_not_in_tree)

        # While MST is not formed
        while len(nodes_in_tree) > self.num_nodes:
            # Edges crossing the cut
            edges_crossing_cut = [(u,v) for u in nodes_in_tree for v in self.adj_map[u].difference(nodes_in_tree)]

            # Select a random edge that crosses the cut
            new_edge = np.random.choice(edges_crossing_cut)

            mst_edges.append(new_edge)
            nodes_in_tree.add(new_edge[1])
            nodes_not_in_tree.remove(new_edge[1])
            print('Nodes in tree:', *nodes_in_tree)
            print('Nodes not in tree:', *nodes_not_in_tree)
        
        return mst_edges
    

def ReadInputFile(f_path):
    # Read the data from file
    with open(f_path, 'r') as f:
        data = f.readlines()
    
    # Save number of nodes
    num_nodes = int(data[0].strip())

    # Save adjacency list
    edges = [[int(n) for n in line.strip().split()] for line in data[1:]]

    return num_nodes, edges


def CompleteATree1(num_nodes, edges):
        cc_map = {i+1:set([i+1]) for i in range(num_nodes)}

        for pair in edges:
            u,v = pair
            new_cc = cc_map[u].union(cc_map[v])

            for e in new_cc:
                cc_map[e] = new_cc

        connected_components = set(frozenset(s) for k,s in cc_map.items())
        # print('Connected components:', *connected_components)

        return len(connected_components) - 1


def CompleteATree2(num_nodes, edges):
    return num_nodes - len(edges) - 1


if __name__ == '__main__':
    input_f = sys.argv[1]

    num_nodes, edges = ReadInputFile(input_f)

    edges_to_for_tree1 = CompleteATree1(num_nodes, edges)
    edges_to_for_tree2 = CompleteATree2(num_nodes, edges)

    print(f'There are {edges_to_for_tree2} edges to complete the tree')