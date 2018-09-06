class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("This restaurant's name is " + self.restaurant_name +
              ", and it specialize in " + self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is opening")

    def set_number_served(self, set_number):
        self.number_served = set_number

    def increment_number_served(self, increment_number, total_number):
        if self.number_served <= total_number:
            self.number_served += increment_number
        else:
            print("Sorry , we don't recepte guest any more.")
