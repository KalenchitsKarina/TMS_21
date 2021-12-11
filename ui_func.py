from exceptions import WrongSignException
from func import Math

def run():

    print ('''_____________________\n
      СALCULATOR''')

    while True:
        print ('_____________________')
        try:
            sign = Math.my_sign()
        except WrongSignException:
            print ('Wrong sign!')
            continue
        
        if sign == '0':
            break
        try:
            a = int (input('Enter a : '))
            b = int (input('Enter b : '))
        except ValueError:
            print ('Invalid input type. You should enter numbers.')
            continue
        val = Math (a, b)

        if sign == '+':
            result = val.sum()
        elif sign == '-':
            result = val.sub()
        elif sign == '*':
            result = val.mul()
        elif sign == '/':
            try:
                result = val.div ()
            except ZeroDivisionError:
                print ('division by zero.')
                continue
        try:
            print (f'result = {result}')
        except UnboundLocalError:
            print ('result = None')
            

