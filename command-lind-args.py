import sys 

def add(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2

def mul(num1, num2):
    return num1*num2

num1 =float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == 'add':
    print(add(num1, num2))
elif operation == 'sub':
    print(sub(num1, num2))
else:
    print(mul(num1, num2))