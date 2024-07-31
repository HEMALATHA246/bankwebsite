def show_balance(balance):
    print(f"Your balance is {balance:}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("That is not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter an amount to withdraw: "))
    if amount > balance:
        print("That is not a valid amount")
        return 0
    elif amount < 0:
        print("Insufficient funds!")
        return 0
    else:
        return amount

balance = 0
is_running = True

while is_running:
    print("_____________________")
    print("\nBanking program")
    print("1. Show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        show_balance(balance)
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw(balance)
    elif choice == "4":
        print("Exiting program.")
        is_running = False
        print("________________")
    else:
        print("That is not a valid choice.")
        print("___________________")
    
    print("Have a nice day!")
if __name__ == '____main___':
    main()

