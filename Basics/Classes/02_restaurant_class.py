class Restaurant:
    """ Restaurant name and type of cuisine they have. """
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """ Print the details of the restaurant. """
        print(f"The {self.name} restaurant is {self.cuisine_type}.")

    def open_restaurant(self):
        """ Print that the restaurant is open. """
        print(f"{(self.name).title()} is open!")

rest_01 = Restaurant("Curricanes", "Seafood")
print(f"The name of the restaurant is: {rest_01.name}")
rest_01.describe_restaurant()
rest_01.open_restaurant()

