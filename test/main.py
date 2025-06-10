#calculator with 'if' , 'else' and 'elif'
print('                         **********CALCULATOR**********')
x = int(input('Enter your first number: '))
operator = input('Enter your operator: ')
y = int(input('Enter your second number: '))
if operator == '+':
    answer = x + y
elif operator == '-':
    answer = x - y
elif operator == '*':
    answer = x * y
elif operator == '/':
    answer = x / y
elif operator == '^':
    answer = x ** y
else: print('Try other operators')
try:
    print(f'Your answer is {answer} ')
except:
    print('Try again')