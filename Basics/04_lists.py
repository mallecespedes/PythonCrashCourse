# Write names

my_friends = ["Cecy" , "Ana Luisa", "Ana Patty", "Griselda"]

# Print each name
# OPTION A
index = 0
while index < len(my_friends):
    print(my_friends[index])
    index = index + 1

# OPTION B
for i in my_friends:
    print(i)

# Print a message using each name
for i in my_friends:
    print(f"Hello {i}")

# Add elements to the list
my_friends.append("Mari")
print(my_friends)

my_friends.insert(1, "Norma")
print(my_friends)

# Sort the list
my_friends.sort()
print(my_friends)

# Find the length of a list
print(len(my_friends))
