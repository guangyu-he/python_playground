class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} has {self.cuisine_type} food!")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is opening!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment


if __name__ == "__main__":
    restaurant = Restaurant("H&H", "Chinese")
    print(restaurant.restaurant_name, restaurant.cuisine_type)
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
    print(restaurant.number_served)
    restaurant.set_number_served(10)
    print(f"new number: {restaurant.number_served}")
    restaurant.increment_number_served(2)
    print(restaurant.number_served)
