stroka=input('Enter your string : ').split()

for i in range (len(stroka)//2):
    f=stroka[-i-1]
    stroka[-i-1]=stroka[i]
    stroka[i]=f
stroka=" ".join(stroka)
print(stroka)
    

