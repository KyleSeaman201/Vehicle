#This code uses OOP principles of inheritance

class Vehicle:
    def __init__(self, wheels, miles, make, model, year):
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = False

    def sell(self):
        if self.sold_on == True:
            print("This item has been sold")
        else:
            self.sold_on = True

    def sale_price(self):
        if self.sold_on:
            return 0.0  
        return 4000 * self.wheels

    def purchase_price(self):
        return self.flat_rate - (.10 * self.miles)

    def getDescription(self):
        sale_price=self.sale_price()
        return "{} {} {} - {} miles >>> ${}".format(self.make, self.model, self.year,self.miles, sale_price)


class Car(Vehicle):
    def __init__(self, wheels, miles, make, model, year, gear, color):
        Vehicle.__init__(self, wheels, miles, make, model, year)
        self.gear = gear
        self.color = color
        self.flat_rate = 7500

    def getDescription(self):
        sale_price=self.sale_price()
        return "{} {} {} - {}, {} miles >>> ${}".format(self.make, self.model, self.year, self.color, self.miles, sale_price)

class Truck(Vehicle):
    def __init__(self, seats, wheels, miles, make, model, year):
        Vehicle.__init__(self, wheels, miles, make, model, year)
        self.seats=seats
        self.flat_rate = 9000

    def getDescription(self):
        sale_price=self.sale_price()
        return "{} {} {}, {} miles - {} seats >>> ${}".format(self.make, self.model, self.year,self.miles, self.seats, sale_price)

