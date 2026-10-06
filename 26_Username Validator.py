# Problem — Username Validator

# Write a function:

# validate_username(username)

# A username is valid only if:

# Its length is between 5 and 15 characters.
# It contains no spaces.
# It contains the character "_".
# It does not start with a number.

# Example:

# validate_username("ahmed_25")

# Output:

# Valid username

# But:

# validate_username("ahmed 25")

# Output:

# Invalid username

# And:

# validate_username("25_ahmed")

# Output:

# Invalid username

  
def vali_username(username):
  is_nospace=True
  char_=False
  start_nonum=True
  
  for c in username:
    
    if c.isspace():
      is_nospace=False
    if c == '_':
      char_=True
      
  if username[0].isdigit():
    start_nonum=False

  if 5<=len(username)<15 and is_nospace and char_ and start_nonum:
    return "Valid Username"
  else:
    return "Invalid Username"
    
print(vali_username("0ahmed_25"))
