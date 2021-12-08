class My_Time:

    def __init__ (self, hours = None, minutes = None, seconds = None):
        if type(hours) == type(minutes) == type(seconds) == int:
            self._hours = hours
            self._minutes = minutes
            self._seconds = seconds
        elif type(hours) == str:
            ls = hours.split(':')
            self._hours = int(ls[0])
            self._minutes = int(ls[1])
            self._seconds = int(ls[2])
        elif hours == minutes == seconds == None:
            self._hours = 0
            self._minutes = 0
            self._seconds = 0
        elif isinstance (hours, My_Time):
            self._hours = hours._hours
            self._minutes = hours._minutes
            self._seconds = hours._seconds

    def print_time (self):
        if self._hours < 24 and self._minutes < 60 and self._seconds < 60:
            print (f'{self._hours}:{self._minutes}:{self._seconds}')
        else:
            if self._seconds >= 60:
                self._minutes += self._seconds // 60
                self._seconds %= 60
            if self._minutes >= 60:
                self._hours += self._minutes // 60 
                self._minutes %= 60
            if self._hours >= 24:
                self._hours %= 24
            print (f'{self._hours}:{self._minutes}:{self._seconds}')

    def __eq__(self, other):
        return self._hours == other._hours and self._minutes == other._minutes and self._seconds == other._seconds

    def __ne__(self, other: object) -> bool:
        return self._hours != other._hours or self._minutes != other._minutes or self._seconds != other._seconds

    def __gt__ (self, other):
        return ((self._hours * 60) + self._minutes) * 60 + self._seconds > ((other._hours * 60) + other._minutes) * 60 + other._seconds

    def __lt__ (self, other):
        return ((self._hours * 60) + self._minutes) * 60 + self._seconds < ((other._hours * 60) + other._minutes) * 60 + other._seconds

    def __ge__ (self, other):
        return ((self._hours * 60) + self._minutes) * 60 + self._seconds >= ((other._hours * 60) + other._minutes) * 60 + other._seconds

    def __le__ (self, other):
        return ((self._hours * 60) + self._minutes) * 60 + self._seconds <= ((other._hours * 60) + other._minutes) * 60 + other._seconds

    def __add__ (self, other):
        self._seconds += other._seconds
        if self._seconds >= 60:
            self._minutes += 1
            self._seconds %= 60
        self._minutes += other._minutes
        if self._minutes >= 60:
            self._hours += self._minutes // 60 
            self._minutes %= 60
        self._hours += other._hours
        if self._hours >= 24:
            self._hours %= 24
        return My_Time(self._hours, self._minutes, self._seconds)

    def __sub__ (self, other):
        self._seconds -= other._seconds
        if self._seconds <= 0:
            self._minutes -= self._minutes // 60
            self._seconds += 60
        self._minutes -= other._minutes
        if self._minutes <= 0:
            self._hours -= 1
            self._minutes += 60
        self._hours -= other._hours
        if self._hours <= 0:
            self._hours += 24
        return My_Time(self._hours, self._minutes, self._seconds)

    def __mul__ (self, other):
        self._seconds *= other
        self._minutes *= other
        self._hours *= other
        return My_Time(self._hours, self._minutes, self._seconds)

def main():
    t1 = My_Time(22, 11, 12)
    t2 = My_Time('12:22:11')
    t3 = My_Time()
    t4 = My_Time (28, 17, 18)
    t5 = t2

    t1.print_time()
    t2.print_time()
    t3.print_time()
    t4.print_time()
    t5.print_time()

    if t1 < t2:
        print ('False')
    else:
        print ('True') 

    if t4 > t3:
        print ('True')
    else:
        print ('False')

    if t2 == t5:
        print ('True')

    if t2 != t4:
        print ('True')

    if t5 >= t2:
        print ('True')

    t2 += t4
    t2.print_time()
    t2 -= t4
    t2.print_time()
    t4 *= 3
    t4.print_time()
     

if __name__ == '__main__':
    main()