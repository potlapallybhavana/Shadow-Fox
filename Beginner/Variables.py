"""
Beginner Task 1: Variables
- Create variable `pi = 22/7` and print its type
- Try assigning to a variable named `for` (explain error)
- Compute Simple Interest (SI) for 3 years: SI = (P*R*T)/100
"""

def simple_interest(p, r, t=3):
    """Return simple interest for principal p, rate r (percent), time t (years)."""
    return (p * r * t) / 100

if __name__ == "__main__":
    # 1) pi and type
    pi = 22/7
    print("pi:", pi, "| type:", type(pi).__name__)

    # 2) reserved keyword explanation
    # The following would raise a SyntaxError because 'for' is a reserved keyword in Python:
    # for = 4   # <-- DON'T DO THIS
    # Instead, use a different name:
    for_value = 4
    print("for_value:", for_value, "(We cannot use 'for' as a variable name because it's a keyword.)")

    # 3) Simple Interest demo
    P = 10000  # principal
    R = 7.5    # annual rate in percent
    T = 3      # years
    si = simple_interest(P, R, T)
    print(f"Simple Interest for P={P}, R={R}%, T={T} years =", si)
