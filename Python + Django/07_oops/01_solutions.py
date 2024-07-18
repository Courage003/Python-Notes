class Car:

    total_car = 0  #keeping count of cars in class Car
    def __init__(self, brand, model):  #Now you can pass parameters
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"    

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    
#Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size  

    def fuel_type(self):
        return "Electric Charge"      

my_tesla = ElectricCar("Tesla", "Model S", "*5kWh")

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))
#print(my_tesla.full_name())
#print(my_tesla.__brand)  #privatisation by putting __
#print(my_tesla.get_brand())
print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
safariThree = Car("Tata", "Nexon")
print(safari.fuel_type())


print(Car.total_car)

print(Car.general_description())
  #static method leads to accessed by classes only not the objects - One of the Decorators in python

#safari.model = "City"
#print(safari.model)  #property decorator (hiding access and providing it for some specifications, reducing any cases of overwriting)

#my_car = Car("Toyota", "Corolla")
#print(my_car.brand) 
#print(my_car.model)

#my_new_car = Car("Tata", "Safari")
#print(my_new_car.model)
#print(my_new_car.full_name())

#self this keyword in javascript
#points to objects inside class

#__init__ is also called as constructor



class Battery:
    def battery_info(self):
        return "This is battery"


class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass



my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())