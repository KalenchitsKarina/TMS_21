m=input('Enter m : ')
n=input('Enter n : ')

while True:
    if m.isdigit()==True and n.isdigit()==True:
        m=int(m)
        n=int(n)
        break
    else:
        print ('"n" or "m" is not digit! Please, try again.')
        m=input('Enter m : ')
        n=input('Enter n : ')
        continue
for i in range(m,n):
    print (i,': ',end="")
    for j in range(2,i):
        if i%j==0:
            print(j,end=" ")
    print(end="\n")