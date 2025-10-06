import streamlit as st
from analyzer import recurrence_tree
from utils import master_theorem
from visualizer import plot_cost_bar

st.title("🧮 Recursion Tree & Recurrence Relation Analyzer")

a = st.number_input("Enter value of a (subproblems):", min_value=1, value=2)
b = st.number_input("Enter value of b (division factor):", min_value=1, value=2)
n = st.number_input("Enter problem size (n):", min_value=1, value=64)
f_exp = st.text_input("Enter f(n) expression (use 'n' as variable):", "n")

def f(n):
    try:
        return eval(f_exp, {"n": n, "math": __import__("math")})
    except Exception:
        return 0

if st.button("Analyze"):
    levels, total = recurrence_tree(a, b, f, n)
    st.write(f"**Total Cost:** {total}")
    st.write(f"**Level-wise Cost:** {levels}")
    st.write(f"**Master Theorem Complexity:** {master_theorem(a, b, 1)}")
    fig = plot_cost_bar(levels)
    st.pyplot(fig)