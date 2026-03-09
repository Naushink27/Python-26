#Remove duplicate elements from a list and print the unique elements.

print("Remove duplicate elements from a list and print the unique elements!")

numbers=list()
for i in range(7):
    number=int(input("Please enter a number: "))
    numbers.append(number)


for i in numbers:
    if numbers.count(i) > 1:
        numbers.remove(i)
print("The unique elements in the list are: ", numbers)