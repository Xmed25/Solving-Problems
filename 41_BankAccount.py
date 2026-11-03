import random as rn
import string as st

class BankAccount:
    def __init__(self, name, balance,gmail,phone):
        self.name = name
        self._balance = balance
        self.gmail=gmail
        self.phone=phone

    def deposit(self):
        try:
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                self._balance += amount
                print(f"Your Current Balance: {self._balance:.2f} EGP")
            else:
                print("Amount must be positive.")

        except ValueError:
            print("Please enter a valid number.")

    def withdraw(self):
        try:
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Amount must be positive.")

            elif amount <= self._balance:
                self._balance -= amount
                print(f"Your Current Balance: {self._balance:.2f} EGP")

            else:
                print("Insufficient balance.")

        except ValueError:
            print("Please enter a valid amount.")


    def information(self,account_number):
            print(f"\nAccount ID: {account_number}")
            print(f"Account Holder: {self.name}")
            print(f"Gmail: {self.gmail[0:4]+len(self.gmail[4:])*'*'}")
            print(f"Phone: +20{self.phone}")
            print(f"Current Balance: {self._balance:.2f} EGP")





def account_number():
        acc_num=st.ascii_letters+st.digits+st.ascii_uppercase
        acc_id="".join(rn.choice(acc_num)for _ in range(5))
        return acc_id
    
account_number=account_number()



def displaying():

    name =input("Enter Your Name: ").strip().capitalize()
    gmail=input("Enter Your Gmail: ").strip().capitalize()
    while True:

        try:
            phone=int(input("Enter Your Phone: "))
            if len(str(phone))==10:
                break
            else:
                print("Invalid Number")
                continue
        except ValueError:
            print("Invalid Number")
            continue

    try:
        balance = float(input("Enter your initial balance: "))

        if balance < 0:
            print("Balance cannot be negative.")
            return

        person = BankAccount(name,balance,gmail,phone)

        while True:

            print("\n1. Account Information")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            try:
                choice = int(input("Choose an option: "))

                if choice == 1:
                    person.information(account_number)

                elif choice == 2:
                    person.deposit()

                elif choice == 3:
                    person.withdraw()
                
                elif choice == 1:
                    print("GoodBye!")
                    break

                else:
                    print("Invalid choice.")

            except ValueError:
                print("Please enter a valid option.")

    except ValueError:
        print("Please enter a valid balance.")


displaying()
