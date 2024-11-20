class ATM:
    def __init__(self, initial_balance=1000, pin="1234"):
        self.balance = initial_balance
        self.pin = pin
        self.transaction_history = []
    
    def check_pin(self, entered_pin):
        """Checks if the entered PIN is correct."""
        return self.pin == entered_pin

    def display_balance(self):
        """Displays the current balance."""
        print(f"Your current balance is: ${self.balance}")
        self.transaction_history.append(f"Checked balance: ${self.balance}")

    def deposit(self, amount):
        """Deposits the specified amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully.")
            self.transaction_history.append(f"Deposited: ${amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """Withdraws the specified amount from the account if sufficient funds are available."""
        if amount > self.balance:
            print("Insufficient funds for this transaction.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
            self.transaction_history.append(f"Withdrew: ${amount}")

    def change_pin(self, old_pin, new_pin):
        """Changes the account PIN if the old PIN matches."""
        if self.check_pin(old_pin):
            self.pin = new_pin
            print("PIN changed successfully.")
            self.transaction_history.append("PIN changed.")
        else:
            print("Incorrect PIN entered.")

    def show_transaction_history(self):
        """Displays the history of all transactions."""
        if not self.transaction_history:
            print("No transactions available.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)


def main():
    atm = ATM()
    print("Welcome to the ATM Simulator")
    
    # Request PIN to start
    entered_pin = input("Please enter your PIN: ")
    if not atm.check_pin(entered_pin):
        print("Incorrect PIN. Access denied.")
        return

    # Main menu
    while True:
        print("\nATM Menu:")
        print("1. Balance Inquiry")
        print("2. Deposit Cash")
        print("3. Withdraw Cash")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            atm.display_balance()
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: "))
                atm.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: "))
                atm.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == "4":
            old_pin = input("Enter current PIN: ")
            new_pin = input("Enter new PIN: ")
            atm.change_pin(old_pin, new_pin)
        elif choice == "5":
            atm.show_transaction_history()
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
