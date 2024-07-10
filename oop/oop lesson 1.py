class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Default attribute value

    def get_descriptive_name(self):
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
           self.odometer_reading += miles
        
first_car = Car("Mercedes", "C200", 2017)
print(first_car.get_descriptive_name())
first_car.read_odometer()
first_car.update_odometer(70000)
first_car.read_odometer()
first_car.increment_odometer(10000)
first_car.read_odometer()