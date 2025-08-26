"""
Beginner Task 6: Dictionary
1) List of friends -> list of tuples (name, length).
2) Trip expenses comparison and analysis.
"""

def names_with_length(names):
    return [(n, len(n)) for n in names]

def compare_expenses(your_expenses: dict, partner_expenses: dict):
    # totals
    your_total = sum(your_expenses.values())
    partner_total = sum(partner_expenses.values())
    # who spent more
    spender = "You" if your_total > partner_total else ("Partner" if partner_total > your_total else "Both equal")
    # category with max difference
    all_keys = set(your_expenses) | set(partner_expenses)
    diffs = {k: abs(your_expenses.get(k,0) - partner_expenses.get(k,0)) for k in all_keys}
    max_cat = max(diffs, key=diffs.get)
    return your_total, partner_total, spender, max_cat, diffs[max_cat]

if __name__ == "__main__":
    friends = ["Aditya", "Bhavana", "Chirag", "Diya", "Eshan"]
    print("Names with length:", names_with_length(friends))

    your_expenses = {
        "Hotel": 1200,
        "Food": 800,
        "Transportation": 500,
        "Attractions": 300,
        "Miscellaneous": 200
    }
    partner_expenses = {
        "Hotel": 1000,
        "Food": 900,
        "Transportation": 600,
        "Attractions": 400,
        "Miscellaneous": 150
    }
    yt, pt, who, cat, diff = compare_expenses(your_expenses, partner_expenses)
    print(f"Your total: {yt}, Partner total: {pt}")
    print("Who spent more:", who)
    print(f"Largest difference: {cat} by {diff}")
