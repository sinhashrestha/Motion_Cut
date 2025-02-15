import csv
from datetime import datetime
expenses = []

def add_expense(date, amount, category, description):
    expense = {
        'date': date,
        'amount': float(amount),
        'category': category,
        'description': description
    }
    expenses.append(expense)

def save_expenses_to_file(filename='expenses.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'amount', 'category', 'description'])
        writer.writeheader()
        writer.writerows(expenses)

def load_expenses_from_file(filename='expenses.csv'):
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def summarize_expenses_by_category():
    summary = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount
    return summary

def summarize_expenses_by_month():
    summary = {}
    for expense in expenses:
        date = datetime.strptime(expense['date'], '%Y-%m-%d')
        month = date.strftime('%Y-%m')
        amount = expense['amount']
        if month in summary:
            summary[month] += amount
        else:
            summary[month] = amount
    return summary

def main():
    global expenses
    expenses = load_expenses_from_file()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Summary")
        print("4. Save and Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            amount = input("Enter amount: ")
            category = input("Enter category (e.g., food, transportation, entertainment): ")
            description = input("Enter description: ")
            add_expense(date, amount, category, description)

        elif choice == '2':
            monthly_summary = summarize_expenses_by_month()
            for month, total in monthly_summary.items():
                print(f"{month}: {total:.2f}")

        elif choice == '3':
            category_summary = summarize_expenses_by_category()
            for category, total in category_summary.items():
                print(f"{category}: {total:.2f}")

        elif choice == '4':
            save_expenses_to_file()
            print("Expenses saved. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
