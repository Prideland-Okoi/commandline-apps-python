import json
from datetime import datetime

accounts = [
    {
        "Name": "John Doe",
        "Account Number": "123456789",
        "Account Type": "Savings",
        "Balance": 1000,
        "Pin": 1234,
        "Transactions": []
    },
    {
        "Name": "Jane Doe",
        "Account Number": "987654321",
        "Account Type": "Checking",
        "Balance": 2000,
        "Pin": 5678,
        "Transactions": []
    },
    {
        "Name": "Bob Smith",
        "Account Number": "192837465",
        "Account Type": "Savings",
        "Balance": 3000,
        "Pin": 2468,
        "Transactions": []
    }
]

def login():
    account_number = input("Enter your account number: ")
    pin = int(input("Enter your pin: "))
    for account in accounts:
        if account["Account Number"] == account_number and account["Pin"] == pin:
            return account
    print("Invalid account number or pin!")
    return None

def export_to_json(account):
    data = {key: value for key, value in account.items() if key != 'Pin'}
    with open(f"{account['Name'].replace(' ', '_')}.json", 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Account data exported to {account['Name'].replace(' ', '_')}.json")

def print_receipt(account, transaction_type, amount, other_account=None):
    print("\n" + "="*30)
    print("Transaction Receipt")
    print("="*30)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Account Number: {account['Account Number']}")
    print(f"Transaction Type: {transaction_type}")
    if transaction_type == 'Transfer':
        print(f"Transferred To: {other_account['Name']}")
    print(f"Amount: ${amount}")
    print(f"New Balance: ${account['Balance']}")
    print("="*30 + "\n")

def main():
    account = login()
    if not account:
        return

    while True:
        print("Welcome to the ATM!")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. View Transaction History")
        print("6. View Account Details")
        print("7. Export to JSON")
        print("8. Change Pin")
        print("9. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print(f"Your balance is: ${account['Balance']}")
        elif choice == 2:
            amount = int(input("Enter the amount to withdraw: "))
            if amount > account["Balance"]:
                print("Insufficient balance!")
            else:
                account["Balance"] -= amount
                account["Transactions"].append({"Type": "Withdraw", "Amount": amount, "Date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                print(f"${amount} withdrawn successfully!")
                print_receipt(account, 'Withdraw', amount)
        elif choice == 3:
            amount = int(input("Enter the amount to deposit: "))
            account["Balance"] += amount
            account["Transactions"].append({"Type": "Deposit", "Amount": amount, "Date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            print(f"${amount} deposited successfully!")
            print_receipt(account, 'Deposit', amount)
        elif choice == 4:
            other_account_number = input("Enter the other account number: ")
            other_account = None
            for acc in accounts:
                if acc["Account Number"] == other_account_number:
                    other_account = acc
                    break
            if not other_account:
                print("Invalid account number!")
            else:
                amount = int(input("Enter the amount to transfer: "))
                if amount > account["Balance"]:
                    print("Insufficient balance!")
                else:
                    account["Balance"] -= amount
                    other_account["Balance"] += amount
                    account["Transactions"].append({"Type": "Transfer", "Amount": amount, "To": other_account['Name'], "Date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                    other_account["Transactions"].append({"Type": "Received", "Amount": amount, "From": account['Name'], "Date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                    print(f"${amount} transferred successfully!")
                    print_receipt(account, 'Transfer', amount, other_account)
        elif choice == 5:
            print("Transaction History:")
            for transaction in account["Transactions"]:
                print(transaction)
        elif choice == 6:
            print("Account Details:")
            for key, value in account.items():
                if key not in ["Pin", "Transactions"]:
                    print(f"{key}: {value}")
        elif choice == 7:
            export_to_json(account)
        elif choice == 8:
            new_pin = int(input("Enter your new pin: "))
            confirm_pin = int(input("Confirm your new pin: "))
            if new_pin != confirm_pin:
                print("Pins do not match!")
            else:
                account["Pin"] = new_pin
                print("Pin changed successfully!")
        elif choice == 9:
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
