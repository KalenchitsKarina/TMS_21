
def duim_cm(a):
    return a*2.538

def cm_duim(a):
    return a*0.394

def mile_km(a):
    return a*1.609

def km_mile(a):
    return a*0.622

def lb_kg(a):    #фунты--кг
    return a*0.454

def kg_lb(a):
    return a*2.205

def ounce_gr(a): #унция--гр
    return a*28.35

def gr_ounce(a):
    return a*0.35274//10

def gallon_litr(a):
    return a*3.78541

def litr_gallon(a):
    return a*0.26417

def pint_litr(a):
    return a*2

def litr_pint(a):
    return a*0.5

def menu():
    print ('\t Выберите нужный вариант конвертирования :')
    print ('''
            0. Выход
            1. Дюймы в сантиметры
            2. Сантиметры в дюймы
            3. Мили в километры
            4. Километры в мили
            5. Фунты в килограммы
            6. Килограммы в фунты
            7. Унции в граммы
            8. Граммы в унции
            9. Галлон в литры
            10. Литры в галлоны
            11. Пинты в литры
            12. Литры в пинты
    ''')
    a=input('\t(0 - 12) : ')
    if a !='0':
        zn=input('\tВведите значение : ')
        if zn.isdigit() == 1:
            zn = int(zn)
        else :
            print ('\tВы ввели неверное число')
            return 1
    if a == '1':
        print ('\t',duim_cm(zn),'сантиметров')
    elif a == '2':
        print ('\t',cm_duim(zn),'дюймов')
    elif a == '3':
        print ('\t',mile_km(zn),'километров')
    elif a == '4':
        print ('\t',km_mile(zn),'миль')
    elif a == '5':
        print ('\t',lb_kg(zn),'килограмм')
    elif a == '6':
        print ('\t',kg_lb(zn),'фунт')
    elif a == '7':
        print ('\t',ounce_gr(zn),'гра')
    elif a == '8':
        print ('\t',gr_ounce(zn),'унций')
    elif a == '9':
        print ('\t',gallon_litr(zn),'литров')
    elif a == '10':
        print ('\t',litr_gallon(zn),'гвллон')
    elif a == '11':
        print ('\t',pint_litr(zn),'литров')
    elif a == '12':
        print ('\t',litr_pint(zn),'пинт')
    elif a == '0':
        return 0
    else :
        print ('\tНекорректное значение')


def main ():
    while True:
        b = menu()
        if b == 0:
            break
        if b ==1 :
            continue
        print ('___________________________________________________________________\n')

if  __name__ == '__main__':
    main()
