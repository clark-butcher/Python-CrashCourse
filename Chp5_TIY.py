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

# age = 18
# age2 = 21
# print(age <= 20 and age2 >= 19)
# print(age == 20 or age2 == 20)
# print(age == 18 or age2 == 21)
# print(age == 28 or age2 == 21)
#
# bad_dogs = ['spike','bandit','carl']
# dog = 'bonnie'
# if dog not in bad_dogs:
#     print(f"{dog.title()}, you're a good dog")
# for dog in bad_dogs:
#     print(f"{dog.title()}, get in your crate")

# alien_color = 'green'
# if alien_color == 'green':
#     print("Congrats, Player! You just won 5 points")
#
# alien_color = 'yellow'
# if alien_color == 'green':
#     print("Congrats, Player! You just won 5 points")

# alien_color = 'red'
# if alien_color == 'green':
#     print("You just earned 5 points")
# else:
#     print("You just earned 10 points")

# alien_color = 'green'
# if alien_color == 'green':
#     print("You just earned 5 points")
# elif alien_color == 'yellow':
#     print("You just earned 10 points")
# elif alien_color == 'red':
#     print("You just earned 15 points")
#
# alien_color = 'yellow'
# if alien_color == 'green':
#     print("You just earned 5 points")
# elif alien_color == 'yellow':
#     print("You just earned 10 points")
# elif alien_color == 'red':
#     print("You just earned 15 points")
#
# alien_color = 'red'
# if alien_color == 'green':
#     print("You just earned 5 points")
# elif alien_color == 'yellow':
#     print("You just earned 10 points")
# elif alien_color == 'red':
#     print("You just earned 15 points")

age = 66

if age < 2:
    print('This person is a baby')
elif age < 4 and age >= 2:
    print('This person is a toddler')
elif age < 13 and age >= 4:
    print('This person is a kid')
elif age < 20 and age >= 13:
    print('This person is a teenager')
elif age < 65 and age >= 20:
    print('This person is an adult')
else:
    print('This person is an elder')

favorite_fruits = ['Mangosteen','Orange','Apple','Blueberry','Blackberry']
if 'Mangosteen' in favorite_fruits:
    print("I love mangosteen.")
if 'Orange' in favorite_fruits:
    print("I love Oranges.")
if 'Strawberry' in favorite_fruits:
    print("I love Strawberry.")
if 'Bananna' in favorite_fruits:
    print('I love banannas.')
if 'raspberry' in favorite_fruits:
    print('I love raspberry')
if 'Apple' in favorite_fruits:
    print('I Love apples')