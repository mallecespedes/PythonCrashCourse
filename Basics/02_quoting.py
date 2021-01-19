# Personal message
name = "Alan"
message = "Would you like some coffee?"

print(f"Hello {name}. {message}")

# Name cases: lowercase, uppercase, title case.
print(name.upper())
print(name.lower())
print(name.title())

# Quote and author in variable.
print(f"{name} said he would like some coffee and a cookie.")

# Stripping names
name_right = f"{name}\t"
name_left = f"\t{name}"
name_break = f"\n{name}"

print(name_right.rstrip())
print(name_left.lstrip())
print(name_break.strip())