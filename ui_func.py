from func import sum
from func import sub
from func import mul
from func import div
import ui_func

print ('''_______________
Choose an action !
1. sum
2. subtract
3. multiply
4. divide
_______________''')
while True:
    sign = input ('+,-,*,/ : ')
    if sign == '0':
        break
    a = int (input('Enter a : '))
    b = int (input('Enter b : '))
    if sign == '+':
        result = sum(a,b)
    if sign == '-':
        result = sub(a,b)
    if sign == '*':
        result = mul(a,b)
    if sign == '/':
        result = div (a,b)
    
    
    print (f'result = {result}')

