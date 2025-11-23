from unreliable_car import UnreliableCar


def main():
    my_unreliablecar = UnreliableCar("GTA", 100, 65)
    print(my_unreliablecar)
    my_unreliablecar.drive(60)
    print(my_unreliablecar)

main()
