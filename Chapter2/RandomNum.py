import random
import string
# print(random.randrange(1,10))
# print(random.random())

# Random float in range
# print(random.uniform(1.5, 5.5))

list1 = ["sachin","rahul","muskan"]
# print(random.choice(list1))
# k=3 print three items can repeat
# print(random.choices(list1,k=3))

# use sample when you don't want any repetetion
# print(random.sample(list1,2))

# Use suffle method when you want to choose a random order
# random.shuffle(list1)
# print(list1)

# dice = random.randint(1,6)
# print(f"You get number {dice}")

# if dice == 6:
#     print("you won")

# Generate Random Password
# character = string.ascii_letters + string.digits + string.punctuation
# password = ''.join(random.choices(character,k=12))
# print(password)

# weighted random choice
# weights = [0.1,0.3,0.6]
# print(random.choices(list1,weights=weights, k=1))

# list2 = ["sachin","rahul","ravi","rakesh","shubham"]
# print("winner",random.sample(list2,2))

# count = 0
# while True:
#     count += 1
#     if random.choice(['head','tail']) == 'head' :
#         print(f"You got head after {count} tosses")
#         break

random.seed(43)
num = random.randint(1,1000)
print(num)