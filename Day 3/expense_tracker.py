expenses = {
    'food': 0,
    'travel': 0,
    'shopping': 0,
    'Bills': 0,
    "other": 0,
}

food = int(input("Enter your food expense: "))
travel = int(input("Enter your travel expense: "))
shopping = int(input("Enter your Shopping expense: "))
bills = int(input("Enter your bills expense: "))
other = int(input("Enter your other expense: "))

expenses.update({
     'food': food,
    'travel': travel,
    'shopping': shopping,
    'Bills': bills,
    "other": other,
})

def total_expense(expense):
    return sum(expense.values())

def highest_expense(expense):
    return max(expense, key = expense.get)

def average_expense(expense):
    return sum(expense.values()) / len(expense)

print(f'Total Expense: {total_expense(expenses)}')

print(f'Highest Expense: {highest_expense(expenses)}')

print(f'Average Expense: {average_expense(expenses)}')