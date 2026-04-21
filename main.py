import pandas as pd

# Sample financial transactions
data = [
    ["Cash", 10000, 0],
    ["Sales Revenue", 0, 10000],
    ["Expense", 3000, 0],
    ["Cash", 0, 3000],
]

df = pd.DataFrame(data, columns=["Account", "Debit", "Credit"])

print("\n📘 Journal Entries:")
print(df)

# Trial Balance
trial = df.groupby("Account").sum()
trial["Balance"] = trial["Debit"] - trial["Credit"]

print("\n📊 Trial Balance:")
print(trial)

# Profit & Loss
revenue = trial.loc["Sales Revenue"]["Credit"]
expense = trial.loc["Expense"]["Debit"]
profit = revenue - expense

print("\n📈 Profit & Loss Statement:")
print(f"Revenue: {revenue}")
print(f"Expense: {expense}")
print(f"Net Profit: {profit}")

# Balance Sheet
cash_balance = trial.loc["Cash"]["Balance"]

print("\n📑 Balance Sheet:")
print(f"Assets (Cash): {cash_balance}")
print(f"Equity (Profit): {profit}")