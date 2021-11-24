class User:

    def __init__(self, first_name, last_name, user_identity):
        #Initialize the object and name attributes
        self.fname = first_name
        self.lname = last_name
        self.uid = user_identity

    def describe_user(self):
        #Print and describe all attributes of the user
        print('User First name: ', self.fname)
        print('User Last name: ', self.lname)
        print('User ID: ', self.uid)

    def greet_user(self):
        #Print a pleasant greeting to the user
        print(f'Welcome {self.fname} {self.lname} to the program!')

johny = User('Johny', 'Silverhand', 'JSilvo')
billy = User('Billy', 'Joel', 'Fatmama69')
sarah = User('Sarah', 'Jennings', 'Sarah88')

johny.describe_user()
johny.greet_user()

billy.describe_user()
billy.greet_user()

sarah.describe_user()
sarah.greet_user()



        
        
