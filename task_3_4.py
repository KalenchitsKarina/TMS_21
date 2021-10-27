str=input(('Enter your strring :'))
mid=len(str)//2
print(str[mid])
if str[0]==str[mid]:
    new_str=str[1:-1:]
    print(new_str)
