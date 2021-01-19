# Create functions and pass parameters into them

def favorite_book():
    """ Print favorite book """
    book = input("What is your favorite book? ")
    print(f"Your favorite book is {book.title()}. That's awesome!")

# favorite_book()

def city_country(city, country):
    """ Print the name of a city and its country """
    print(f"{city}, {country}")

city_country("Cd. Mexico", "Mexico")
city_country("Washington DC", "United States")
city_country("Madrid", "España")

# Create a list with album names
album = []

def make_album(music_list):
    """ Print the albums registered """
    if music_list:
        print("The albums registered are: ")
        for album in music_list:
            print(f"- {album}")

while True:
    album_name = input("Enter the name of an album: ")
    if album_name.lower() == "q":
        break
    
    if album_name != "":
        album.append(album_name)

make_album(album)

# Obtain velocity
def velocity(dist, time):
    """ Given the distance in meters and time in seconds, obtain the velocity. """
    return(f"{str(dist/time)} m/s")

vel = velocity(9, 2)
print(vel)

# Pass arbitrary number of arguments
def make_pizza(*toppings):
    """ Print the list of toppings requested """
    print(toppings)

make_pizza("pepperoni", "pineapple", "extra cheese")