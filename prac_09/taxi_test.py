from taxi import Taxi

my_taxi=Taxi("Prius1",100)
my_taxi.drive(40)
print(my_taxi)
print(f"current fare is $ {my_taxi.get_fare()}")
my_taxi.start_fare()
my_taxi.add_fuel(40)
my_taxi.drive(100)
print(my_taxi)
print(f"current fare is $ {my_taxi.get_fare()}")