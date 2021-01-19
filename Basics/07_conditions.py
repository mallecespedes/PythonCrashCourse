# Create some conditions 

my_age = 25

if my_age >= 21:
    print("Congratulations, you can have a driver's license.")
else:
    print("You can't have a driver's license.")

name = "Malle"

if "a" in name.lower():
    print("The name contains the letter a")
else:
    print("The name doesn't contain the letter a")

# Build program that'll define park charges depending on the hour
# 0-2 hours $10
# 2-5 hours $15
# above 5 hours $18

hours_parked = 2
if hours_parked <= 2:
    charge = 10
elif hours_parked <= 5:
    charge = 15
else:
    charge = 18

print(f"Pay ${charge}")

# Alien colors exercise
alien_color = "red"

if alien_color == "green":
    print("You earned 5 points.")
elif alien_color ==  "yellow":
    print("You earned 10 points")
else:
    print("You earned 15 points")

# Checking availability of toppings for pizza
available_toppings = ["mushrooms", "olives", "pepperoni", "pineapple", "ham", "extra cheese"]
requested_toppings = ["olives", "french fries", "extra cheese"]

for topping in requested_toppings:
    if topping in available_toppings:
        print(f"Adding {topping} to your pizza!")
    else: 
        print(f"Sorry, we don't have {topping}")