# Smart Command-Line Calculator

# Problem: Build a calculator that accepts two numbers and an operator, performs the requested calculation, and lets the user continue until they choose to exit.

# Requirements
# - Support addition, subtraction, multiplication, division, exponentiation, and modulus.
# - Validate the operator and handle division by zero.
# - Allow repeated calculations using a loop.
# - Display a useful error message for invalid input.
# - Ask the user whether to continue after each operation.
# Example
# Enter first number: 12
# Enter operator (+, -, *, /, **, %): /
# Enter second number: 3
# Result: 4.0

# Continue? (yes/no): no





def Questions():
  while True:
    try:
      
      num1=float(input("Enter first number: "))
      
      operator=input("Enter operator (+, -, *, /, **, %) : ")
      if operator not in ["+", "-", "*", "/", "**", "%"]:
              print("Error: Invalid operator!")
              continue
      num2=float(input("Enter second number: "))
      
      print(operations(num1,operator,num2))
      continu=input("Continue? (yes/no): ")
      if continu.lower().strip()=="no":
        break
      else:
        continue
      
    except ValueError:
      print("Error ! Please enter valid numbers!")
      continue
      
def operations(num1,operator,num2):
  
  if operator=='+':
    result=num1+num2

    
  elif operator=='-':
    result=num1-num2
 
    
  elif operator=='*':
    result=num1*num2

    
  elif operator=='/':
    try:
      result=num1/num2

    except ZeroDivisionError :
      return "You Can Not Divide by Zero"
      
  elif operator=='**':
    result=num1**num2

    
  elif operator=="%":
    try:
      result=num1%num2

    except ZeroDivisionError :
      return "You can not divide by zero"

  else:
    return "Invalid Operator !"
    
  return f"Result : {result}"


Questions()
