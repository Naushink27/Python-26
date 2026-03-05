#Task4: Password retry system

password="python123"

for attempt in range(3):
    user=input("Enter the password:")
    if user==password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.")
else:    print("Access denied. Too many attempts.")