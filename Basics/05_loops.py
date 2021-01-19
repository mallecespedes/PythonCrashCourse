# Store types of pizza in a list and print them
pizzas = ["pepperoni", "three meats", "ham"]

for pizza in pizzas:
    print(f"OMG, I love {pizza} pizza!")

print("Pizza is great.")

# Use range to make a list of numbers
for number in range(1, 6):
    print(number)

# Create a list with the squares of a list that contains even numbers
even_numbers = list(range(2, 11, 2))
squares = []
for value in even_numbers:
    squares.append(value ** 2)

print(squares)

# Perform simple statistics with a list of numbers
print(min(squares))
print(max(squares))
print(sum(squares))

# Sum a million numbers
my_million_list = range(1, 1000001)
print(sum(my_million_list))

# Slice a list
odd_numbers = list(range(1, 20, 2))
print(odd_numbers[0:3])

# Copy a list into another list
new_odd_numbers = odd_numbers[:]
print(new_odd_numbers)
