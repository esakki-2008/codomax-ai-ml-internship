"""ExpenseTracker Pro - Codomax Module 2 Mini Project."""
from datetime import datetime
from pathlib import Path
import csv

DATA_FILE = Path(__file__).with_name("expenses.csv")
CATEGORIES = ("Food", "Travel", "Shopping", "Bills", "Education", "Health", "Other")

def load_expenses():
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def save_expenses(expenses):
    with DATA_FILE.open("w", newline="", encoding="utf-8") as file:
        fields = ["date", "category", "description", "amount"]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(expenses)

def add_expense(expenses):
    print("\n--- Add Expense ---")
    category = input(f"Category {CATEGORIES}: ").strip().title()
    if category not in CATEGORIES:
        category = "Other"
    description = input("Description: ").strip() or "General expense"
    try:
        amount = float(input("Amount (₹): "))
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("❌ Please enter a valid positive amount.")
        return
    expenses.append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "category": category,
        "description": description,
        "amount": f"{amount:.2f}",
    })
    save_expenses(expenses)
    print("✅ Expense added successfully.")

def view_expenses(expenses):
    print("\n--- Expense History ---")
    if not expenses:
        print("No expenses recorded yet.")
        return
    print(f"{'Date':<18} {'Category':<12} {'Description':<25} {'Amount':>12}")
    print("-" * 72)
    for e in expenses:
        print(f"{e['date']:<18} {e['category']:<12} {e['description'][:24]:<25} ₹{float(e['amount']):>10.2f}")

def show_summary(expenses):
    print("\n--- Financial Summary ---")
    if not expenses:
        print("No expense data available.")
        return
    total = sum(float(e["amount"]) for e in expenses)
    average = total / len(expenses)
    highest = max(expenses, key=lambda e: float(e["amount"]))
    print(f"Total expenses : ₹{total:,.2f}")
    print(f"Transactions   : {len(expenses)}")
    print(f"Average expense: ₹{average:,.2f}")
    print(f"Largest expense: ₹{float(highest['amount']):,.2f} ({highest['description']})")

def category_report(expenses):
    print("\n--- Category Report ---")
    if not expenses:
        print("No expense data available.")
        return
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + float(e["amount"])
    total = sum(totals.values())
    for category, amount in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        print(f"{category:<12} ₹{amount:>10,.2f} ({amount / total * 100:>5.1f}%)")

def main():
    expenses = load_expenses()
    while True:
        print("\n" + "=" * 48)
        print("           EXPENSETRACKER PRO")
        print("=" * 48)
        print("1. Add Expense\n2. View Expenses\n3. Financial Summary\n4. Category Report\n5. Exit")
        choice = input("\nSelect an option: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            category_report(expenses)
        elif choice == "5":
            print("\nThank you for using ExpenseTracker Pro. 👋")
            break
        else:
            print("❌ Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
