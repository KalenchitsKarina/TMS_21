#Дано число. Найти сумму и произведение его цифр.

n=input('Enter the number : ')
sum=0
proizv=1

if n.isdigit()==True:
    for i in range (len(n)):
        sum+=int(n[i])
        proizv*=int(n[i])
    print('Sum of digits : ',sum)
    print('Product of n : ', proizv)
else:
    print('n is not a digit')

