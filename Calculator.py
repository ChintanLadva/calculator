def addition(n1, n2):
    return n1+n2
def subtration (n1, n2):
    return n1-n2
def multiplication(n1, n2):
    return n1*n2
def divition(n1, n2):
    if n2==0:
        return "Cannot divide by zero"
    return n1/n2
print("Simple Calculater")

n1 = float(input("Enter N1 number:- "))
n2 = float(input("Enter N2 number:- "))
oper = input("Enter operater (+,-,*,/):- ")

if oper == '+':
  print('Result:',addition(n1, n2))
elif oper == '-':
  print('Result:',subtration(n1, n2))
elif oper == '*':
  print('Result:',multiplication(n1, n2))
elif oper == '/':
  print('Result:', divition(n1, n2))
else:
  print('Invalid operator')