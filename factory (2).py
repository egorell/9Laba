class Bike(object):
    def bike(self):
        raise NotImplementedError()


class USA(Bike):
    def bike(self):
        print ('USA\'s bike')


class RUS(Bike):
    def bike(self):
        print ('RUS\'s bike')


class CreateBike(object):
    def create_bike(self, type_):
        raise NotImplementedError()


class MyCreateBike(CreateBike):
    def create_bike(self, type_):
        if type_ == 'USA':
            return USA()
        elif type_ == 'RUS':
            return RUS()
        else:
            return Bike()


b1 = MyCreateBike()
b1.create_bike('USA').bike()
b1.create_bike('RUS').bike()
try:
    b1.create_bike('Canda').bike()
except:
    print("NotImplementedError")
