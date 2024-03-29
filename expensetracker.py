import datetime

# Expense class to hold each expense entry:
class Expense:
    def __init__(self, type, name, date, amount):
        self.type = type
        self.name = name
        self.date = date
        self.amount = amount

    def __repr__(self):
        return f"{self.type} | {self.name} | {self.date} | ${self.amount:.2f}"

# List to store expenses:
expenses = []

# Function to add an expense:
def add_expense(type, name, date, amount):
    expense = Expense(type, name, date, amount)
    expenses.append(expense)
    print("Expense added successfully.")

# Function to list all expenses:
def list_expenses():
    print("Type | Name | Date | Amount")
    for expense in expenses:
        print(expense)

# Function to delete an expense:
def delete_expense(name):
    global expenses
    expenses = [expense for expense in expenses if expense.name != name]
    print("Expense deleted successfully.")

# Function to get user input and perform actions:
def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add an expense")
        print("2. List all expenses")
        print("3. Delete an expense")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            type = input("Enter the type of expense: ")
            name = input("Enter the name of the expense: ")
            date_input = input("Enter the date of the expense (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
            amount = float(input("Enter the amount of the expense: "))
            add_expense(type, name, date, amount)

        elif choice == '2':
            list_expenses()

        elif choice == '3':
            name = input("Enter the name of the expense to delete: ")
            delete_expense(name)

        elif choice == '4':
            print("Exiting the Expense Tracker.")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

