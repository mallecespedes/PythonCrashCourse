class Dog:
    """ A simple attempt to model a dog. """

    def __init__(self, name, age):
        """ Initialize name and age attributes. """
        self.name = name
        self.age = age

    def sit(self):
        """ Simulate a dog sitting in response to a command. """
        print(f"{self.name} is now sitting")
    
    def roll_over(self):
        """ Simulate rolling over in response to a command. """
        print(f"{self.name} rolled over")

# A function that is part of a class is a method. 
# The init method is a special method that Python runs automatically whenever we create a new instance
#  based on the Dog class. The self parameter is required in the method definition and must come first.
#  It must be included in the definition because when Python calls this method later, the method will 
#  automatically pass the seld argument. It is a reference to the instance itself. 
#  Any variable prefixed with self is available to every method in the class. Variables that are 
#  accessible through instances like this are called attributes. 

my_dog = Dog("Willie", 6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} y/o")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog("Muñeca", 15)
print(f"Your dog's name is {your_dog.name}")
your_dog.sit()