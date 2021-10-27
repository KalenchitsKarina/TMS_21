'''
Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}). 
Чтобы получить список ключей - использовать метод .keys()
(подсказка: создается новый ключ с цифрой в конце, старый удаляется)
'''
dc={'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
keys=list(dc.keys())

print(dc)

for i in range (0,len(keys)):
    dc[keys[i]+str(len(keys[i]))]=dc[keys[i]]
    del dc[keys[i]]
    i+=1
print (dc)

'''
dict={'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
key1=list(dict.keys())
el=0
while el<len(key1):
    dict[key1[el]+str(len(key1[el]))]=dict[key1[el]]
    del dict[key1[el]]
    el+=1
print (dict)
'''