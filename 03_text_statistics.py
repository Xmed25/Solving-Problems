# 🟢 Problem 3 : Text Statistics 
# Write a program that asks the user to enter a sentence.

# Print:
# Total number of characters.
# Total number of words.
# Number of vowels.
# Number of digits.
# Number of spaces.
# Number of uppercase letters.
# Number of lowercase letters.
# Example
# Input:
# Hello Ahmed 2026
# Output:
# Characters: 16
# Words: 3
# Vowels: 4
# Digits: 4
# Spaces: 2
# Uppercase: 2
# Lowercase: 8


sen=input("Enter a Sentence: ")


vowels=0
digits=0
spaces=0
upper=0
lower=0

for s in sen:
    if s.isalpha():
        pass
    if s.lower() in "aeiou":
        vowels+=1
    if s.isdigit():
        digits+=1
    if s.isspace():
        spaces+=1
    if s.isupper():
        upper+=1
    if s.islower():
        lower+=1        
print(f"Characters: {len(sen)}")
print(f"Words: {len(sen.split())}")
print(f"Vowels: {vowels}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Uppercase: {upper}")
print(f"Lowercase: {lower}")
