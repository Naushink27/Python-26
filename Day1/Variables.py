#Python Variables baiscs
x=7
y=8
print(x)
print(y)
print(x+y)

#Variable can only start with a letter or an underscore
#Variable can only contain letters, numbers and underscores
#Variable names are case sensitive

name="Naushin"
print(name)

a=10
A=20
#This will create two different variables a and A
print(a)


# python allows you to assign multiple variables in one line

x,y,z=1,2,3
print(x)
print(y)
print(z)

#You can also assign the same value to multiple variables in one line
a=b=c=100
print(a)

#Python is a dynamically typed language, which means you don't have to declare the type of variable. The type is determined at runtime based on the value assigned to it.
x=10
print(type(x)) # Output: <class 'int'>

x="Hello"
print(type(x)) # Output: <class 'str'>

n=3.14
n="pi"
#the type of n is now str
print(type(n)) # Output: <class 'str'>

m=5
#print(n+m) # This will raise a TypeError because you cannot add a string and an integer

#Can create variable with type declaration

c=int(10)
print(c) # Output: 10
print(type(c)) # Output: <class 'int'>

