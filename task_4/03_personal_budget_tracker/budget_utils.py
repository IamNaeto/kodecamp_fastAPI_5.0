from collections import defaultdict

def group_by_category(transactions):
    grouped = defaultdict(list)
    for t in transactions:
        grouped[t.category].append(t)
    return grouped

def calculate_totals(transactions):
    totals = {}
    grouped = group_by_category(transactions)
    for category, items in grouped.items():
        totals[category] = round(sum(t.amount for t in items), 2)
    return totals
