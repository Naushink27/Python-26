#Task3:Even number list

even_list=[x for x in range(21) if x%2==0] # List comprehension to generate a list of even numbers from 0 to 20
print("The list of even numbers from 0 to 20 is: ", even_list)


odd_list=[x for x in range(21) if x%2!=0] # List comprehension to generate a list of odd numbers from 0 to 20
print("The list of odd numbers from 0 to 20 is: ", odd_list)