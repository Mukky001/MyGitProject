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

# Strings in Arrays
x = "God did!"
print (x[4])
print ("********************************")

# Looping through a string
for y in "Banana":
    print(y)
print ("********************************")

# String lenght
x = "Banana"
print(len(x))
print ("********************************")

# Checking for string presence
txt = "Best I ever had!"
print("ever" in txt)
print ("********************************")

# checking only if string is present
txt = "Best I ever had!"
if "ever" in txt:
    print("yes, 'ever' is present")
print ("********************************")

# Checking When string is not present
txt = "Best I ever had!"
print("ever" not in txt)
print ("********************************")

# Checking and printing when string is not present
txt = "Best I ever had!"
if "free" not in txt:
    print("No, 'free' is not present")
print ("********************************")

# Slicing (Note: Position 7 not includec)
x = "God, World!"
print (x [2:7])
print ("********************************")

# Slicing from start (Note: Position 6 not includec)
x = "God, World!"
print (x [:6])
print ("********************************")

# Slicing to the end 
x = "God, World!"
print (x [2:])
print ("********************************")

# Negative indexing (Note: position -6 not included)
x = "God, World!"
print (x [-6:-2])
print ("********************************")





