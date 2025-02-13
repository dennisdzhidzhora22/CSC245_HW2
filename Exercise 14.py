# Reverse a string
s = input("Enter a string: ")
s2 = ""

for char in s:
    s2 = char + s2

print("Reversed string: " + s2)