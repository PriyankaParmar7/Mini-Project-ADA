import math

def calculate_factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)

def fibonacci(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def parse_function_expression(expr):
    # This function will parse a function expression like "n^2" or "log(n)"
    # and return a callable function. This is a placeholder for future implementation.
    pass

def evaluate_function(f, n):
    # This function will evaluate the function f at the value n.
    # This is a placeholder for future implementation.
    pass

def master_theorem(a, b, f_power):
    """
    Applies Master Theorem for recurrence of the form T(n) = aT(n/b) + O(n^f_power)
    """
    log_val = math.log(a, b)
    if f_power < log_val:
        return f"Case 1: O(n^{round(log_val,2)})"
    elif abs(f_power - log_val) < 1e-6:
        return f"Case 2: O(n^{f_power} log n)"
    else:
        return f"Case 3: O(n^{f_power})"