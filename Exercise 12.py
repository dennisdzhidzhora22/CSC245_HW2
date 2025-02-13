# Count vowels in a string
s = input("Enter a string: ")
vowelCount = 0

for char in s.lower():
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vowelCount += 1

print(f"There are {vowelCount} vowels in the string.")