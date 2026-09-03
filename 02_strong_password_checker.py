# 🟢 Problem 2 : Strong Password Checker 

# Write a program that checks whether a password is strong.
# A strong password must satisfy all of the following:

# At least 8 characters long.
# Contains at least one uppercase letter.
# Contains at least one lowercase letter.
# Contains at least one digit.
# Contains at least one special character (@, #, $, %).
# Example
# Input:
# Hello123@

# Output:
# Strong Password
# Input:
# hello123

# Output:
# Weak Password


import random as rn
import string as st
x=st.ascii_uppercase
y=st.ascii_lowercase
o=st.digits

gen=rn.choices(x,k=3)+rn.choices(y,k=2)+rn.choices(o,k=4)+rn.choices('@#$%',k=2)
rn.shuffle(gen)
gen="".join(gen)

is_upper=False
is_lower=False
is_digit=False
is_punc=False
password=input("Create a password: ")
for p in password:
    if p.isupper():
        is_upper=True
    if p.islower():
        is_lower=True
    if p.isdigit():
        is_digit=True
    if p in '@#$%':
        is_punc=True
if len(password)>=8 and is_lower and is_upper and is_digit and is_punc:
    print("Strong Password !")
else:
    print("Weak Password !")
    print(f"""
Suggestion Password:
{gen}
    """)
