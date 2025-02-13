# List Operations
myList = [4, 2, 8, 10, 5, 6]

myList.append(14)

myList.remove(6)

print("The length of the list is " + str(len(myList)))

print("List before sorting: " + str(myList))
myList.sort()
print("Sorted list: " + str(myList))