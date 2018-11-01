#Mary Green
#04/29/18
#Unit 10
#CarPrg.py
#Designing a car class that accepts information from the use of the year model, make and speed.

#creating the car class
class Car:
#creating the constructor
    def __init__(self, Year, makeCar):
        self.__yearModel = Year
        self.__make = makeCar
        self.__speed = 0
#creating the accessors and mutators definitions
    def set_yearModel(self, Year):
        self.__yearModel = Year

    def set_make(self, makeCar):
        self.__make = makeCar

    def set_speed(self, speedCar):
        self.__speed = speedCar

    def get_yearModel(self):
        return self.__yearModel

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed
#defining the accelerate and brake methods
    def accelerate(self):
        self.__speed = self.__speed + 5

    def brake(self):
        self.__speed = self.__speed - 5
#creating a car object and fields with values passing it to the __init__ method.
def main():
    MyCar = Car("2013", "Toyota")

    index = 0
    brake = False
#creating a while loop to display the accelerate speed
    while index < 5:
        MyCar.accelerate()
        print('This is the accelerate speed of the Toyota 2013:', MyCar.get_speed())
        index = index + 1
        if index == 4:
            brake = True
    if brake == True:
        i = 0
#creating a while loop to display the brake speed
        while i < 5:
            MyCar.brake()
            print('This is the brake speed of the Toyota 2013:', MyCar.get_speed())
            i = i + 1
    





#calling the main function
main()

#Program Output:
# This is the accelerate speed of the Toyota 2013: 5, 10, 15, 20, 25
#This is the brake speed of the Toyota 2013: 25, 20, 15, 10, 5, 0


    
