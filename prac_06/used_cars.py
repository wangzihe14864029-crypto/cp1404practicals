"""
CP1404 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.

Estimate: 10 minutes
Actual: 15 minutes
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use Car class."""
    my_car = Car("MyCar", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # 1. Create a new Car object called "limo" with 100 units of fuel
    limo = Car("Limo", 100)

    # 2. Add 20 more units of fuel using add_fuel method
    limo.add_fuel(20)

    # 3. Print the amount of fuel in the car
    print(f"{limo.name} has fuel: {limo.fuel}")

    # 4. Attempt to drive the car 115 km
    limo.drive(115)

    # 5~7. Print the limo object to check __str__ works
    print(limo)


main()