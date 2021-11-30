class car:
    __speed = 0

    def __init__ (self, brand ,model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year
        

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    def increase_speed (self):
        self.__speed += 5

    def reduce_speed (self):
        self.__speed -= 5

    def stop (self):
        self.__speed = 0

    def reverse (self):
        self.__speed *= (-1)

class sport_car(car):

    def increase_speed (self):
        self.__speed += 15

    def reduce_speed (self):
        self.__speed -= 15

class gruz_car(car):

    def increase_speed (self):
        if self.__speed +5 < 60:
            self.__speed += 5
        else:
            print ('don\'t risk it')
            self.__speed = 60

class electro_car (car):
    __charge_level = 100
    __speed_limit = 40

    def charge (self):
        self.__charge_level = 100
        self.__speed = 0

    def increase_speed (self):
        if self.__charge_level < 50:
            if self.__speed + 5 > self.__speed_limit:
                print (f'Low battery! Speed limit {self.__speed_limit} km/h')
        else : 
            self.__speed += 5
            self.__charge_level =- 10
        

def main ():
    my_car = car ('suzuki','e212',2006)
    my_car.increase_speed()
    print(my_car.get_speed())
    my_el_car = electro_car('bmw','i8',2015)
    my_el_car.increase_speed()
    print(my_el_car.get_speed())
    

if __name__ == '__main__':
    main()

