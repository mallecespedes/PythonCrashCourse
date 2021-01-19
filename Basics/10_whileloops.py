# Pizza toppings entering
print("Hi! Welcome to Malle's Pizzas!")
print("Enter the toppings you want in the pizza, one by one. When you are finished, type 'exit'.")
flag = True
toppings = []
i = 0

while flag:
    topping = (input(f"Enter the topping #{i + 1}: "))
    if topping.lower() == 'exit':
        break

    toppings.append(topping)
    i += 1

if toppings:
    print("The topics of your pizza will be: ")
    for topping in toppings:
        print(f"- {topping}")
