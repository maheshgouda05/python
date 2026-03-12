import getpass

Account = {
    '1mj24cd024': {'name': 'mahesh', 'pin': '9686', 'balance': 2000, 'history': []},
    '1mj24cd035': {'name': 'sainath', 'pin': '0066', 'balance': 10000, 'history': []}
}

while True:
    print("\n------ ATM MENU ------")
    print("1. Balance Enquiry")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Transaction History")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        acc = input("Enter account number: ")

        if acc in Account:
            pin = getpass.getpass("Enter PIN: ")

            if pin == Account[acc]['pin']:
                print("Account Holder:", Account[acc]['name'])
                print("Balance:", Account[acc]['balance'])
            else:
                print("Incorrect PIN")
        else:
            print("Account not found")

    elif choice == 2:
        acc = input("Enter account number: ")

        if acc in Account:
            pin = getpass.getpass("Enter PIN: ")

            if pin == Account[acc]['pin']:
                amount = int(input("Enter amount to withdraw: "))

                if amount > Account[acc]['balance']:
                    print("Insufficient balance")
                else:
                    Account[acc]['balance'] -= amount
                    Account[acc]['history'].append(f"Withdraw: {amount}")
                    print("Please collect your cash")
                    print("Remaining Balance:", Account[acc]['balance'])
            else:
                print("Incorrect PIN")
        else:
            print("Account not found")

    elif choice == 3:
        acc = input("Enter account number: ")

        if acc in Account:
            pin = getpass.getpass("Enter PIN: ")

            if pin == Account[acc]['pin']:
                amount = int(input("Enter amount to deposit: "))
                Account[acc]['balance'] += amount
                Account[acc]['history'].append(f"Deposit: {amount}")

                print("Amount deposited successfully")
                print("Updated Balance:", Account[acc]['balance'])
            else:
                print("Incorrect PIN")
        else:
            print("Account not found")

    elif choice == 4:
        acc = input("Enter account number: ")

        if acc in Account:
            print("\nTransaction History:")
            for h in Account[acc]['history']:
                print(h)
        else:
            print("Account not found")

    elif choice == 5:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")