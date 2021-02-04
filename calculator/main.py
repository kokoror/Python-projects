from art import logo
from replit import clear

print(logo)

def add(n1, n2):
  return n1 + n2

def substract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def division(n1, n2):
  return n1/n2

operation_dic = {
  "+":add,
  "-":substract,
  "*": multiply,
  "/": division
  }

number1 = float(input("What is the first number? "))

continue_cal = True

#the key is the loop will be always true, if continue the calculation, replace the number 1 with calculation result,
# if not continue, clear the screen and ask user to reenter number1
while continue_cal:
  for symbol in operation_dic:
    print(symbol)
  operation_input = input("Pick an operation: ")
  number2 = float(input("What is the next number? "))
  operation = operation_dic[operation_input]
  result = operation(number1, number2)
  print(f"{number1} {operation_input} {number2} = {result}")
  number1 = result

  if_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation\n")
  if if_continue == 'n':
    clear()
    number1 = float(input("What is the first number? "))
    

