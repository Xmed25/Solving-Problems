# Personal Expense Tracker


# Problem: Create a program that records expenses, categorizes spending, and compares expenses with a monthly budget.

# Requirements
# - Ask the user to enter a monthly budget.
# - Record each expense with its description, amount, and category.
# - Store transactions as dictionaries inside a list.
# - Allow the user to add multiple expenses until they choose to stop.
# - Calculate total spending, remaining budget, and average expense.
# - Use comprehensions to filter expenses by category.
# - Use enumerate() to display numbered transactions.
# - Display a warning when spending reaches or exceeds 80% of the budget.
# - Display an alert when the budget is exceeded.
# - Identify unique spending categories using a set.
# Example
# Monthly budget: 5000

# 1. Groceries - 1200 EGP
# 2. Transport - 500 EGP
# 3. Internet - 400 EGP

# Total spent: 2100 EGP
# Remaining budget: 2900 EGP
# Average expense: 700.00 EGP
# Budget status: Within budget




def customerbudget():
    while True:
        try:
            budget = float(input("Monthly Budget (EGP): "))

            if budget <= 0:
                print("Budget must be greater than zero!")
                continue

            break

        except ValueError:
            print("Invalid Number!")

    expenses = []

    while True:
        print("\n--- Add Expense ---")
        print("Type 'stop' to finish.")

        name = input("Expense name: ").strip()

        if name.lower() == "stop":
            break

        if not name:
            print("Expense name cannot be empty!")
            continue

        while True:
            try:
                amount = float(input("Expense amount (EGP): "))

                if amount <= 0:
                    print("Expense must be greater than zero!")
                    continue

                break

            except ValueError:
                print("Invalid Number!")

        category = input("Category: ").strip().title()

        if not category:
            print("Category cannot be empty!")
            continue

        expense = {
            "description": name,
            "amount": amount,
            "category": category
        }

        expenses.append(expense)

        print("Expense added successfully!")

    return expenses, budget


def calculations(expenses, budget):
    total_spending = sum(
        expense["amount"] for expense in expenses
    )

    remaining = budget - total_spending

    average = (
        total_spending / len(expenses)
        if expenses else 0
    )

    print("\n========== EXPENSE REPORT ==========")

    print(f"Monthly budget: {budget:.2f} EGP")

    if expenses:
        print("\n--- Transactions ---")

        for number, expense in enumerate(expenses, start=1):
            print(
                f"{number}. {expense['description']} - "
                f"{expense['amount']:.2f} EGP "
                f"({expense['category']})"
            )
    else:
        print("\nNo expenses recorded.")

    print("\n--- Financial Summary ---")
    print(f"Total spent: {total_spending:.2f} EGP")
    print(f"Remaining budget: {remaining:.2f} EGP")
    print(f"Average expense: {average:.2f} EGP")

    percentage = (total_spending / budget) * 100

    print(f"Budget used: {percentage:.2f}%")

    if total_spending > budget:
        print("ALERT: Budget Exceeded!")

    elif percentage >= 80:
        print("WARNING: You have used 80% or more of your budget!")

    else:
        print("Budget status: Within budget")

    categories = {
        expense["category"] for expense in expenses
    }

    print("\n--- Unique Categories ---")

    if categories:
        for category in sorted(categories):
            print(f"- {category}")
    else:
        print("No categories available.")

    print("\n--- Filter Expenses by Category ---")

    if categories:
        selected_category = input(
            "Enter category to filter: "
        ).strip().title()

        filtered_expenses = [
            expense for expense in expenses
            if expense["category"] == selected_category
        ]

        if filtered_expenses:
            for number, expense in enumerate(
                filtered_expenses, start=1
            ):
                print(
                    f"{number}. {expense['description']} - "
                    f"{expense['amount']:.2f} EGP"
                )

            category_total = sum(
                expense["amount"]
                for expense in filtered_expenses
            )

            print(
                f"Category total: {category_total:.2f} EGP"
            )

        else:
            print("No expenses found in this category.")


def main():
    expenses, budget = customerbudget()
    calculations(expenses, budget)


if __name__ == "__main__":
    main()
