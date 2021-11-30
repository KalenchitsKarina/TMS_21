class student:

    def __init__ (self, name, group, ball) :
        self.__name = name
        self.__group = group
        self.__ball = ball

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_group(self):
        return self.__group

    def set_group(self,group):
        self.__group = group

    def get_ball(self):
        return self.__ball

    def set_ball(self, ball):
        self.__ball = ball

    def print_all_inf(self):
        print (f'a student of group {self.__group} {self.__name} has an average score {self.__ball}!' )
    
    def graduated (self):
        print (f'a student of group {self.__group} {self.__name} graduated from university with average score {self.__ball}! Congrat!' )    

class house:

    def __init__(self,number,kolvo_kv,year):
        self.__number = number
        self.__kolvo_kv = kolvo_kv
        self.__year = year

    def get_number (self):
        return self.__number

    def set_number (self, number):
        self.__number = number

    def get_kolvo_kv (self):
        return self.__kolvo_kv

    def set_kolvo_kv (self, kolvo_kv):
        self.__kolvo_kv = kolvo_kv

    def get_year (self):
        return self.__kolvo_kv

    def set_year (self, year):
        self.__year = year

    def new_year (self):
        self.__year+=1
    
    def info (self):
        print (f'house number {self.__number}, number of flats {self.__kolvo_kv}, {self.__year} year of construction')
   
    def age (self):
        print (2021-self.__year, 'yo')

class table:

    def __init__(self,code,weigh,heigh):
        self.__code = code
        self.__weigh = weigh
        self.__heigh = heigh

    def get_code (self):
        return self.__code

    def set_code (self, code):
            self.__code = code

    def get_weigh (self):
            return self.__weigh

    def set_weigh (self, weigh):
            self.__weigh = weigh       

    def set_heigh (self, heigh):
            self.__heigh = heigh

    def get_heigh (self):
            return self.__heigh

    def broke (self):
        print ('your table broken')
        
    def info (self):
        print (f'vendor code {self.__code}, weigh {self.__weigh}kg, heigh {self.__heigh}cm ')
    
    def lunch (self):
        print ('table is ready for lunch')

class cooker:

    def __init__(self,power,burners,type):
        self.__power = power
        self.__burners = burners
        self.__type = type

    def get_power (self):
        return self.__power

    def set_power (self, power):
            self.__power = power

    def get_burners (self):
            return self.__burners

    def set_burners (self, burners):
            self.__burners = burners       

    def set_type (self, type):
            self.__type = type

    def get_type (self):
            return self.__type

    def broke (self):
        print ('your cooker broken')
        
    def info (self):
        print (f'power {self.__power}, number burners {self.__burners}, type {self.__type}')
    
    def cook (self):
        print ('table is ready for cooking')

class poezd:

    def __init__(self,number,free_places,speed):
        self.__number = number
        self.__free_places = free_places
        self.__speed = speed

    def get_number (self):
        return self.__number

    def set_number (self, number):
            self.__number = number

    def get_free_places (self):
            return self.__free_places

    def set_free_places (self, free_places):
            self.__free_places = free_places       

    def set_speed (self, speed):
            self.__speed = speed

    def get_speed (self):
            return self.__speed

    def increase_speed (self):
        self.__speed += 10
        
    def info (self):
        print (f'train number {self.__number}, free places {self.__free_places}, speed {self.__speed} ')
    
    def reduce_speed (self):
        self.__speed -= 10

def main ():

    stud = student('Ivan',890541,7.9)
    stud.print_all_inf()
    stud.set_group(990541)
    stud.print_all_inf()

    my_home = house(36,190,2003)
    my_home.new_year()
    my_home.info()
    my_home.age()

    desk = table(129228, 20, 110)
    desk.lunch()
    desk.info()
    desk.broke()

    plate = cooker (220, 4, 'electro')
    plate.cook()
    plate.broke()
    plate.info()

    my_poesd = poezd(12, 288, 120)
    my_poesd.info()
    my_poesd.set_speed(90)
    my_poesd.increase_speed()
    my_poesd.info()
        
if __name__ == '__main__':
    main()

