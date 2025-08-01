a = input('Num:  ')
operator = input('Enter Operator (+,-,*,/,%,//):  ')
b = input('Second Num:  ')
a = int(a)
b = int(b)
if operator == '+':
    print(a + b)
elif operator == '-':
    print(a - b)
elif operator == "/":
    print(a / b)
elif operator == '*':
    print(a * b)
elif operator == '%':
    print(a % b)
elif operator == '//':
    print(a // b)
else:
    print('Invalid Operation')
