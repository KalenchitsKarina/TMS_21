guests=int(input('Enter the number of guests: '))

if guests>50:
    print('restaurant')
elif guests>20:
    print('cafe')
elif guests<0:
    print('Please try again')
else:
    print('home')