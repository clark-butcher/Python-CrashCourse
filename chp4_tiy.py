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

cubes = list(range(1,11))
for value in cubes:
    print(value**3)

cubes = [value**3 for value in range(1,11)]
print(cubes)