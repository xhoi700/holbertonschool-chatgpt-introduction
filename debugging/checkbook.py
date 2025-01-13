class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Amount to deposit must be greater than 0.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        self.get_balance()

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount to withdraw must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
            self.get_balance()

    def get_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")

def main():
    print("Welcome to the Checkbook Application!")
    cb = Checkbook()
    while True:
        print("\nWhat would you like to do?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        action = input("Enter your choice (1-4): ")
        if action == '4':
            print("Thank you for using the Checkbook Application. Goodbye!")
            break
        elif action == '1':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action == '2':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action == '3':
            cb.get_balance()
        else:
            print("Invalid choice. Please select an option from 1 to 4.")

if __name__ == "__main__":
    main()
