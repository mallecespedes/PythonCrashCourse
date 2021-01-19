# Store information about a person in a dictionary
person = {"name": "Malle", "age": 25, "nacionality": "mexican", "favorite food": "pasta", "favorite sport": "basketball"}
print(person["name"])
print(person["favorite sport"])

for key, value in person.items():
    print(f"His/her {key} is {value}.")

# Use sort in the looping
favorite_languages = {"Malle": "Python", "Alan": "C++", "Fer": "Java"}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")