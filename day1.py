# my first code

print("hello world!")

# create a new variable

x = 4
y = 4

# print("hasil tambah x dan y:")
# print(f"{x+y}")

# value dari variable dapat berubah jika dibuat variable dengan penamaan yang sama persis

x = 10
x = "satria"

# print("x saat ini adalah:", x)

# casting value variable
x = int(10)
y = str(20)
z = float(30)

print("x bertype: ",type(x))
print("y bertype: ",type(y))
print("z bertype: ",type(z))

#multiple comment
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

print("below is the legal name for variable")
myvar = "myvar"
my_var = "my_var"
_my_var = "_my_var"
myVar = "myVar"
MYVAR = "MYVAR"
myvar2 = "myvar2"

print("python can create multiple values for a variable")

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print("python also can make one value for a many variable")

x = y = z = "Orange"
print(x)
print(y)
print(z)

print("python can unpack collection inside list")

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print("python can print a lot of variable directly in one line")

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)