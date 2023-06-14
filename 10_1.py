import copy
class Car:
    pass
car_1 = Car()
car_1.circle = 4
car_2 = car_1
car_2.circle = 3
print(car_1.circle)

car_3 = copy.copy(car_1)
car_3.circle = 6

print(car_1.circle)
