# Task3: Take a list of numbers as input and print sum 

print("Calculate the sum of a list of numbers!")

numbers=list()
for i in range(5):
    number=int(input("Please enter a number: "))
    numbers.append(number)

total_sum=sum(numbers)
print("The sum of the numbers is: ", total_sum)