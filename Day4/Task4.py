#Task4: Username generator

print("Welcome to the Username Generator!")

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

# Generate the username

username=first_name[0].lower()+"."+last_name.lower()+"123"
print("Generated Username:", username)