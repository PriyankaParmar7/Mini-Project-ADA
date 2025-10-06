import math

def analyze_recurrence(a, b, f, n):
    """
    Analyzes the recurrence relation T(n) = aT(n/b) + f(n) and computes the costs per level.

    Parameters:
    a (int): The number of subproblems.
    b (int): The factor by which the problem size is reduced.
    f (function): The function representing the cost of the work done outside the recursive calls.
    n (int): The size of the problem.

    Returns:
    tuple: A tuple containing the costs per level and the total cost.
    """
    costs = []
    total_cost = 0
    level = 0

    while n > 1:
        cost = a * f(n)
        costs.append(cost)
        total_cost += cost
        n //= b
        level += 1

    return costs, total_cost

def f_example(n):
    """
    Example function for f(n) = n log n.

    Parameters:
    n (int): The size of the problem.

    Returns:
    float: The cost of the function.
    """
    return n * (math.log(n) if n > 1 else 0)

def recurrence_tree(a, b, f, n):
    """
    Generate the cost of each level in a recursion tree for recurrence T(n) = aT(n/b) + f(n).

    Parameters:
    a (int): The number of subproblems.
    b (int): The factor by which the problem size is reduced.
    f (function): The function representing the cost of the work done outside the recursive calls.
    n (int): The size of the problem.

    Returns:
    tuple: A tuple containing the costs per level and the total cost.
    """
    levels = []
    level = 0
    current_n = n

    while current_n >= 1:
        nodes = a ** level
        cost = nodes * f(current_n)
        levels.append(cost)
        level += 1
        current_n = current_n / b

        if current_n < 1:  # Base case
            break

    total_cost = sum(levels)
    return levels, total_cost

# Example usage
if __name__ == "__main__":
    a = 2
    b = 2
    n = 16
    costs, total = analyze_recurrence(a, b, f_example, n)
    print("Costs per level:", costs)
    print("Total cost:", total)