class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_car_info(self):
        print(f"🚗 Brand: {self.brand}, Model: {self.model}, Price: ₹{self.price}")


# Creating car objects
car1 = Car("Toyota", "Camry", 3000000)
car2 = Car("BMW", "X5", 8000000)

# Display car details
car1.display_car_info()
car2.display_car_info()
