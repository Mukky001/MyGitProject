# print holla amigo
print ("Holla, Amigo!")

print ("********************************")


# Setting of variables in python 
a = 5  # int variable
y = "clay" #string variable
print (a)
print (y)


print ("********************************")
'''
This is a multiline comment
written in more than one line

'''



print ("Buenos dias")

print ("********************************")
# casting (specifying the data type)
a=int(5)
y=str(5)
z=float(5)
print(a)
print(y)
print(z)
print ("********************************")

# Many values to multiple variable
x, y, z = "Black", "White", "Green"
print(x) 
print(y)
print(z)
print ("********************************")

# One value to multiple variable
x = y = z  = "Black"
print(x) 
print(y)
print(z)
print ("********************************")

# Unpacking a collection
colours = ["Black", "Blue", "Green"]
x, y, z = colours
print(x) 
print(y)
print(z)
print ("********************************")

# Output Variables
k = "Sid is adorable"
print(k)
print ("********************************")

x = "Sid"
y = "is"
z = "adorable"
print (x, y, z)
print ("********************************")

x = "Sid "
y = "is "
z = "adorable "
print(x + y + z)
print ("********************************")

x = 3
y = 7
print(x + y)
print ("********************************")

x = 2
y = "Bags"
print(x, y)
print ("********************************")

# Global Variable

x = "Adorable"

def myfunc():
    print("sid is " + x)
myfunc()
print ("********************************") # Not working yet

x = "adorable"
def myfunc():
    x = "beautiful" # can only be used within the function (local variable)
    print("sid is " + x)
myfunc()
print("sid is " + x)
print ("********************************")

# Global veriable
def myfunc():
    global x
    x = "awesome"
myfunc()
print("sid is " + x)   
print ("********************************")  

# Variable conversion
x = 5 # int type
y = 5.0 # float type
z = 1j  # complex

a = float (x) # convert int to float
b = complex (y) # convert float to complex
c = int (x) # convert complex to int

print(a)
print(b)
print(c) 

print (type(a))
print (type(b))
print (type(c))
print ("********************************") 

# Random Number 
import random
print (random.randrange (1, 20))
print ("********************************")


#random

