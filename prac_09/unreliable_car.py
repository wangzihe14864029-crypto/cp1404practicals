from car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name="", fuel=0, reliability=0):
        super().__init__(name,fuel)
        self.reliability=reliability

    def __str__(self):
        return f"{super().__str__()}"
    def drive(self, distance):
        random_reliability = random.random()*100
        if random_reliability < self.reliability:
            distance_drive = super().drive(distance)
        else:
            distance_drive = 0
            print("Reliability error")
        return(distance_drive)