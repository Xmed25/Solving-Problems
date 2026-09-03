# 🟢 Problem 1 — Password Attempts

# Create a password system.
# User has 3 attempts.
# If password is correct:
# Access Granted
# After 3 wrong attempts:
# Account Locked

for times in range(3):
    user=input("USERNAME: ")
    password=input("Password: ")
    if user.lower()=='admin' and password=='12345':
        print("Login Successfully ! ")
        break
    else:
        print("Username or password is incorrect !")
else:
    print("Account Locked !")

<<< with While Loop >>>

attempts=0
while attempts<3:
    user=input("USERNAME: ")
    password=input("Password: ")
    if user.lower()=='admin' and password=='12345':
        print("Login Successfully ! ")
        break
    else:
        print("Username or password is incorrect !")
    attempts+=1
    
else:
    print("Account Locked !")
