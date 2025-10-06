import matplotlib.pyplot as plt
import networkx as nx

def plot_cost_bar(levels):
    fig, ax = plt.subplots()
    ax.bar(range(len(levels)), levels)
    ax.set_title("Recursion Tree Cost per Level")
    ax.set_xlabel("Level")
    ax.set_ylabel("Work (Cost)")
    ax.grid(True)
    return fig

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

    fig, ax = plt.subplots()
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10, ax=ax)
    ax.set_title("Recursion Tree Visualization")
    return fig