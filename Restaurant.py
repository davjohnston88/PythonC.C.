class Restaurant:
    #Class to create a description for different restaurants

    def __init__(self, restaurant_name, cuisine_type):
        #Initialize the current instance and establish parameters
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        #Name and tell what type of restaurant it is
        print(f'{self.name} is a {self.cuisine} style of restaurant.')

    def open_restaurant(self):
        #Say that the restaurant is open
        print(f'{self.name} is currently open right now!\n')

    def full_describe(self):
        #Use both previous methods at once
        self.describe_restaurant()
        self.open_restaurant()

r1 = Restaurant('Billys Pit', 'Southern BBQ')
r2 = Restaurant('Sally Jules', 'Grandma\'s Kitchen')
r3 = Restaurant('Hideki\'s', 'Japanese')

r1.full_describe()
r2.full_describe()
r3.full_describe()


        
