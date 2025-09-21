import pandas as pd

def addExpense():
    new_expense = float(input("Enter a new expense: "))
    item = input("What did you spend the money on? ")
    date = input("What day was it (DD/MM/YYYY): ")

    new_data = pd.DataFrame({
        'expense':[new_expense],
        'item':[item],
        'date':[date],
    })

    new_data.to_csv("ExpenseTracker/array.csv", mode="a", header=False, index=False)

addExpense()

dt = pd.read_csv("ExpenseTracker/array.csv")

print(dt)