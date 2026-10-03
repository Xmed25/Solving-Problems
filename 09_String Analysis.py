# Problem — String Analysis

# Ask the user to enter a word.
# Tasks:
# 1. Print the first character.
# 2. Print the last character.
# 3. Print the length of the word.
# 4. Extract all uppercase characters.
# 5. Extract all lowercase characters.

upper = ""
lower = ""

word = input("Enter a word: ")
print("First character:", word[0])
print("Last character:", word[-1])
print("Length:", len(word))

for x in word:
    if x.isupper():
        upper += x

    if x.islower():
        lower += x

print("Lower:", lower)
print("Upper:", upper)
