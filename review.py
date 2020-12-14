# Printing my name

# print("Miguel Coria")

# Using input to get user's name

# user_name = input("what is your name? \n")

# print(f"Hello {user_name}!!")

# Integers

# print(2+4)

# print(4+9)

# print(3-9)

# print(2 * 5)

# print(type(4 / 5))

# print(type(2+5))

# a float takes up more space than an integer

# print(2 ** 3)

# print(8 // 3)

# print(6 % 4)

# print(round(3.5))

# print(abs(-4.54))

# do not read the dicationary

# do not just try to read the dictionary

# do not try to memorize everything

# understand what exist

# print(bin(5))

# name = "miky"

# print("hi " + name)

# print(f'Hi {name}')

# print(name.title())


# print(li)

# li[0] = "oscar"

# matrix = [[1,2,3], [4,5,6]]


# print(len(li))

# methods

# li.append("nana")

# print(li)

# li.insert(0, "jenni")

# print(li)

# li.remove("jenni")

# print(li)

# li = ["miky", "toti", "leo", "bibi", "bila"]

# print(sorted(li))

# print(li.reverse())

# print(li)

# Dictionary

# Dictionaries are not in order

# dictionary = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4,
#     'e': 5,
#     'list': [1,2,3,4]
# }

# # TUPLE

# my_tuple = (1, 2, 3, 4, 5)

# print(my_tuple.count(1))
# print(my_tuple.index(1))

# my_set = {1, 2, 3, 4, 5, 5}

# print(my_set)

# is_old = True
# is_licences = True

# if is_old and is_licences:
#     print('You are old')
# else:
#     print("you are young")

# print("hi")

# is_friend = False

# can_message = "message allowed" if is_friend else "now allowed to message"

# print(can_message)

# for i in "miky":
#     print(i)

# for item in (1, 2, 3, 4, 5):
#     for x in ['a', 'b', 'c']:
#         print(item, x)


# for item in dictionary.items():
#     print(item)



# for key, value in dictionary.items():
#     print(key, value)

# count = 0

# for item in my_list:
#     count += item

# print(count)


# i = 0
# while i < 50:
#     print(i)
#     i += 1
# else:
#     print("Done printing!!!")

# while True:
#     response = input('What is your name? \n')
#     if (response):
#         break

# dictionary = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4,
#     'e': 5,
#     'list': [1,2,3,4]
# }

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0]
# ]

# fill = "*"
# empty= ''
# for row in picture:
#     for pixel in row:
#         if pixel:
#             print(fill, end="")
#         else:
#             print(empty, end="")
#     print("")

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# new_list = []
# for i in some_list:
#     count = 0
#     for j in some_list:
#         if (i == j):
#             count += 1
#     if count > 1:
#         if i not in new_list:
#             new_list.append(i)

# print(new_list)

# def say_hello(name):
#     print(f'Hello {name}')

# say_hello("miky")

# def sum(num1, num2):
#     return num1 + num2

# print(sum(2, 3))

# def super_func(*args, **kwargs):
#     total = 0
#     for item in kwargs.values():
#         total += item
#     return sum(args) + total

# print(super_func(1, 2, 3, 4, 5, num1=5, num2=5))

# a = "Helllloooooooo"

# if ((n := len(a)) > 10):
#     print(f"too long {n} elements")



# class BigObject:
#     pass

# obj1 = BigObject()

# class PlayerCharacter:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age 

#     def run(self):
#         print('run')

#     def speak(self):
#         print(f'my name is {self._name}, and I am {self._age} years old')

# player1 = PlayerCharacter("cindy", 13)

# print(player1.speak())

# class User:
#     def __init__(self, email):
#         self.email = email
#     def sign_in(self):
#         print('logged in')

# class Wizard(User):
#     def __init__(self, name, power, email):
#         super()
#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f'attacking with power of {self.power}')


# class Archer(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         print(f'attacking with arrows: arrows left: {self.num_arrows}')
#         self.num_arrows = self.num_arrows - 1

# wizard1 = Wizard("miky", 50, 'miguel@miguel.com')
# archer1 = Archer("Robin", 100)

# print(wizard1.email)


# class Toy():
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age

# action_figure = Toy("red", 0)

# is all about seperation of concerns

# what is a pure function

# from functools import reduce

# list1 = [1, 2, 3]
# list2 = [4,5,6]
# def multiply_by2(li):
#     return li * 2

# def check_odd(num):
#     return num % 2 != 0

# def accumulator(acc, item):
#     return acc + item


# new_list = list(map(lambda num: num ** 2, list1))

# print(new_list)

# list1 = [1, 2, 3, 4, 5]

# my_lisst = [char for char in 'hello']

# print(my_lisst)
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicates = (list(set([x for x in some_list if some_list.count(x) > 1])))

# print(duplicates)
# def my_deco(func):
#     def wrap_func(x):
#         print('+++++')
#         func(x)
#         print('+++++')
#     return wrap_func

# @my_deco
# def hello(greeting):
#     print(greeting)


# hello("hola")
# from time import time
# def performance(fn):
#     def wrapper(*args, **kwargs):
#         y1 = time()
#         result = fn(*args, **kwargs)
#         y2 = time()
#         print(f'took {y2-y1} ms')
#         return result
#     return wrapper

# @performance
# def long_time():
#     for i in range(1000000):
#         i * 5


# long_time()


# error handling

# try: 
#     print(1 + "dfa")
# except:
#     print("oops")

# while True:
#     try:
#         age = int(input('What is your age? \n'))
#         print(age)
#     except:
#         print("please enter a number")
#     else:
#         print('Thank you')
#         break

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f"Please enter numbers + {err}")

print(sum('1', 2))





