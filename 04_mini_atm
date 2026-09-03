# 🟢 Problem 4: Mini ATM System 
# Create a console ATM system.
# Initial balance:
# 1000
# Menu:
# ===== ATM =====
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Transfer
# 5. Exit

# Requirements:

# Deposit amount must be greater than 0.
# Withdraw amount must be greater than 0 and not exceed the balance.
# Transfer amount must be greater than 0 and not exceed the balance.
# Keep showing the menu until the user chooses Exit.
# After every successful operation, display the updated balance.
# Display clear error messages for invalid input or insufficient funds.


import time
from datetime import date
import datetime
import random

balance=1000
deposit=0
withdraw=0
transfer=0
card='12255222'
attempts=0
while True:
    print("===== ATM =====")
    print(""" 
1. Check Balance
2. Deposit
3. Withdraw
4. Transfer
5. Exit
""")
    chose=int(input("Enter your Choice: "))
    if chose==1:
        print(f"Your Current Balance: {balance}")
    elif chose==2:
        dep=int(input("Enter your Amount: "))
        if dep>0:
            deposit+=dep
            balance+=dep
            chk=input("Do You want a check ? (y/n) : ")
            if chk.lower()=='y':
                print("Wait a few seconds...\n")
                time.sleep(3)
                print(f"TINKOFF ATM BANK\n")
                print("-----------------")
                print(f"Card:{'*'*4}{card[4:]}")
                today=date.today()
                print(f"Date:{today}")
                current_time = datetime.datetime.now().time()
                print(f"Time:{current_time}")
                print(f'Auth Code:{random.randint(100000,990000)}')
                print("------------------------")
                print("Surcharge: $3.50")
                print(f"Total Debited: ${dep-3.50}")
                print("------------------------")
                print(f"Available Balance:\n${balance}")

        else:
            print("Error !")
    elif chose==3:
        withd=int(input("Enter an Amount: "))
        if withd>0 and withd<=balance:
            balance-=withd
            withdraw+=withd
    elif chose==4:
        _to=int(input("Enter a number of card: "))
        tra=int(input("Enter an amount: "))
        if tra>0 and tra <=balance:
            balance-=tra
            transfer+=tra
    elif chose==5:
        print("Logout Successfull")
        break
    else:
        print("Error !")
        attempts+=1
        if attempts==5:
            print("ATM Locked !") 
            print("Please Try Later")
            break
