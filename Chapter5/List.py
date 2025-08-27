firstList = ["apple", "banana", "cherry"]
# print(type(firstList), firstList)
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# Allow duplicate
# print(len(firstList))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]

# We can also create list using list() constructure
list5 =  list(("Ram", "Lakshman"))
# print(list5)

# We can also indexed list item 
# This will print the last item in the list
# print(list1[-1])

# print(list4[2:4])
# print(list4[:4])
# print(list4[2:])

# We can check that any specified item is presented in the list or not using in

# print("Ram" in list5)
# list5[1] = "Sachin"
# print(list5)

# list5[0:1] = ["sachin", "saurabh"]
# print(list5)
# list5[0:2] = ["pawan"]
# print(list5)

# We can insert any value in any list without replce any other value using insert() you can also select at which index

# list1.insert(2,"Alok")
# print(list1)