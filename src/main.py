from analyzer import recurrence_tree
from utils import master_theorem
from visualizer import plot_cost_bar, plot_recursion_tree

def main():
    a = 2
    b = 2
    n = 64
    def f_n(x): return x  # Non-recursive work: f(n) = n

    levels, total = recurrence_tree(a, b, f_n, n)

    print("\n--- Recursion Tree Analyzer ---")
    for i, cost in enumerate(levels):
        print(f"Level {i}: Cost = {cost:.2f}")

    print(f"\nTotal Cost = {total:.2f}")

    print("\nMaster Theorem Analysis:")
    print(master_theorem(a, b, 1))  # f(n) = n => n^1

    plot_cost_bar(levels)
    plot_recursion_tree(a, b, len(levels), n)

if __name__ == "__main__":
    main()