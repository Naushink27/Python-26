#Task2: Square generator

thislist = [1, 2, 3, 4, 5]

#List comprehension to generate a list of squares

squared_list=[x*x for x in thislist]
print("The original list is: ", thislist)
print("The squared list is: ", squared_list)