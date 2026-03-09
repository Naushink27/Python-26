# Task2: Find largest and smallest number in a list of numbers

print("Check the largest and smallest number in a list of numbers!")

numbers=list()
for i in range(5):
    number=int(input("Please enter a number: "))
    numbers.append(number)

largest=max(numbers)
smallest=min(numbers)
print("The largest number is: ", largest)
print("The smallest number is: ", smallest)