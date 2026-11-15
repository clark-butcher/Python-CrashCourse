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

# age = 66
#
# if age < 2:
#     print('This person is a baby')
# elif age < 4 and age >= 2:
#     print('This person is a toddler')
# elif age < 13 and age >= 4:
#     print('This person is a kid')
# elif age < 20 and age >= 13:
#     print('This person is a teenager')
# elif age < 65 and age >= 20:
#     print('This person is an adult')
# else:
#     print('This person is an elder')
#
# favorite_fruits = ['Mangosteen','Orange','Apple','Blueberry','Blackberry']
# if 'Mangosteen' in favorite_fruits:
#     print("I love mangosteen.")
# if 'Orange' in favorite_fruits:
#     print("I love Oranges.")
# if 'Strawberry' in favorite_fruits:
#     print("I love Strawberry.")
# if 'Bananna' in favorite_fruits:
#     print('I love banannas.')
# if 'raspberry' in favorite_fruits:
#     print('I love raspberry')
# if 'Apple' in favorite_fruits:
#     print('I Love apples')

# user_names = ['Jimmy','Todd','John','admin','jake']
# for name in user_names:
#     if name == 'admin':
#         print("Hello admin, would you like to see a report?")
#     else:
#         print(f"Hello {name}, thank you for logging in.")

# user_names = []
# if user_names:
#     for name in user_names:
#         print(f"Hello {name}, would you like to see a report?")
# else:
#     print(f"We need to find some users!")

# current_users = ['Jimmy','Todd','John','admin','jake']
# new_users = ['Jack','Jane','Thomas','Carlos','jake','Jimmy']
#
# if new_users:
#     for user in new_users:
#         if user in current_users:
#             print(f"{user}, you need a new username")
#         else:
#             print(f"Welcome to the webpage, {user}")

numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")

