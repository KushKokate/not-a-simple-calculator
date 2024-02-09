from art import logo
def add(n1, n2):
  return n1 + n2
def substract(n1, n2):
  return n1 - n2
def multiply (n1, n2):
  return n1 * n2
def divide (n1, n2):
  return n1 / n2
operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide,
}
n1 = int(input("Enter the first value!: "))
n2 = int(input("Enter the second value !: "))
for i in operations:
  print(i)
def calculator():
  print(logo)
should_continue = True
while should_continue:
  operation_symbol = input("Choose any one of the symbols   from above ! : ")
  calculation_func = operations[operation_symbol]
  answer = calculation_func(n1, n2)
  print(f"{n1}{operation_symbol}{n2}={answer}")
  if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
    n1 = answer
else :
  should_continue = False
  calculator()
calculator()

  
  
