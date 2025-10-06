import matplotlib.pyplot as plt
import networkx as nx

def plot_cost_bar(levels):
    plt.bar(range(len(levels)), levels)
    plt.title("Recursion Tree Cost per Level")
    plt.xlabel("Level")
    plt.ylabel("Work (Cost)")
    plt.grid(True)
    plt.show()

def plot_recursion_tree(a, b, depth, n=64):
    G = nx.DiGraph()

    def add_nodes(node, n, d):
        if d == depth:
            return
        for i in range(a):
            child = f"T({int(n/b)})"
            G.add_edge(node, child)
            add_nodes(child, n/b, d + 1)

    root = f"T(n)"
    G.add_node(root)
    add_nodes(root, n, 0)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10)
    plt.title("Recursion Tree Visualization")
    plt.show()