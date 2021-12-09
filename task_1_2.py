#Даны действительные числа x и y. Получить (|x| − |y|)/(1+ |xy|)

x = float(input('Enter x: '))
y = float(input('Enter y: '))
z = (abs(x) - abs(y)) / (1 + abs(x * y))
print('z = %.3f' %z)