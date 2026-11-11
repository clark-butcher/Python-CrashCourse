# cat = 'calico'
# print("is cat == 'calico'? I predict True")
# print(cat == 'calico')
#
# dog = 'golden'
# print("\nis dog == 'golden'? I predict True")
# print(dog == 'golden')
#
# name = "Pat"
# print("\nis name == 'Pat'? I predict True")
# print(name.lower() == 'pat')
#
# drink = "tea"
# print("\nis drink == 'tea'? I predict False")
# print(drink == 'coffee')
#
# color = "red"
# print("\nis color == 'red'? I predict False")
# print(color == 'yellow')

age = 18
age2 = 21
print(age <= 20 and age2 >= 19)
print(age == 20 or age2 == 20)
print(age == 18 or age2 == 21)
print(age == 28 or age2 == 21)

bad_dogs = ['spike','bandit','carl']
dog = 'bonnie'
if dog not in bad_dogs:
    print(f"{dog.title()}, you're a good dog")
for dog in bad_dogs:
    print(f"{dog.title()}, get in your crate")