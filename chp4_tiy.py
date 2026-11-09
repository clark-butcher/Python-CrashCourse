# pizzas = ['pastrami','pepperoni','CBR']
# for pizza in pizzas:
#     print(f"I would like a {pizza}\n")
# print("wow I should stop eating this pizza")
from xml.dom.minidom import ProcessingInstruction

# animals = ['Whale','Dolphin','Orca']
# for animal in animals:
#     print(f"A {animal.lower()} should live in the ocean.")
# print("\nThey are sea creatures. They need water to live")

# twenty = [value+1 for value in range(20)]
# print(twenty)

# millions = []
# for value in range(1,1000000):
#     print(value)
# twenty = []
# for value in range(1,21):
#     print(value)
#
# millions = list(range(1,1000000))
# print(max(millions))
# print(min(millions))
# print(sum(millions))

# odd_numbers = list(range(1,20,2))
# print(odd_numbers)

# multiples = list(range(3,31,3))
# for value in multiples:
#     print(value)

# cubes = list(range(1,11))
# for value in cubes:
#     print(value**3)
#
# cubes = [value**3 for value in range(1,11)]
# print(cubes)

# my_foods = ["chocolate", "Potato", "Carrot", "Pizza","Vanilla"]
# print('The first three items in the list are:')
# print(my_foods[:3])
#
# print('The three items in the middle of my list are:')
# print(my_foods[1:4])
#
# print('The last three items in the list are:')
# print(my_foods[-3:])
#
#
my_pizzas = ['pastrami','pepperoni','CBR']
friend_pizzas = my_pizzas[:]

my_pizzas.append('eggplant')
friend_pizzas.append('hawaiann')
#
# print('my friends favorite pizzas are:')
# print(friend_pizzas[0:])
#
# print('my favorite pizzas are:')
# print(my_pizzas[:])

for pizza in my_pizzas:
    print(f"I like to eat {pizza}")

buffet_foods = ("chicken","fries","bread","pizza","burger")
for food in buffet_foods:
    print(food)
# buffet_foods.append("ice cream")

buffet_foods = ("chicken", "chocolate", "foccacia", "pizza", "burger")
print("\nNew Menu")
for food in buffet_foods:
    print(food)