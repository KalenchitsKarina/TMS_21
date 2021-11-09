str = input ('Enter string : ').split('. ')
new_str = [f'{i} - {str[i]}' for i in range (len(str))]
print (new_str)