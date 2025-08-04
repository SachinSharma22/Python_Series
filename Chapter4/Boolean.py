# Boolean True Statement
# print(bool("sachin"))
# print(bool(1))
# print(bool(True))

# Boolean False Statement
# print(bool(0))
# print(bool({}))
# print(bool(()))
# print(bool([]))
# print(bool(None))
# print(bool(False))

# We can also use this of comparison
# Even empty string is also considered as flase in python
# name = "Sachin"
# if bool(name) :
#     print("You name is",name)
# else:
#     print("your string is wrong or empty")


# if you have an object that is made from a class with a __len__ function that returns 0 or False:

# class myClass:
#     def __len__(self):
#         return 0
    
# myObj = myClass()
# print(bool(myObj))

# Function can also return boolean value

# def myFunc() :
#     return True

# if myFunc:
#     print("Yes")
# else:
#     print("No")

x = 200

print(isinstance(x, int))