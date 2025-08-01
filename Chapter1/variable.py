# a = 5
# print(type(a))
# a = "five"
# print(a)

# You can also choose type of any variable
# a = int(5)
# print(type(a))
# a = str(5)
# print(type(a))

# You can asign multiple values in one line
# x,y,z = "apple", "cherry","mango"
# print(x)
# print(y)
# print(z)

# You can also assign same value for multiple variable

# x = y = z = "sachin"
# print(x)
# print(z)
# print(y)

# You can unpack any list
# fruits = ["apple","banana","mango"]
# a, b, c = fruits
# print(a)
# print(b)
# print(c)

# global variable

# a = 5

# def myFunc() :
#     print(a)

# myFunc()

# a = "awsome"

# def myFunc() :
#     a = "fantastic"
#     print("Python is " + a)

# myFunc()

# print("Python is " + a)

# to create a global varibale inside a function you can use global keyword

def myFun() :
    global a
    a = "sachin"
    print(a)

myFun()
print(a)