# car = input("What type of car are you looking to buy")
# print(f"\nLet me see if I can find you a {car}")
#
# dinner_party = input("How many people are in your dinner party?")
# dinner_party = int(dinner_party)
#
# if dinner_party <= 8:
#     print(f"\nYour table is ready")
# else:
#     print(f"\nYou'll need to wait for table")
#
# number = input("Give me a number. I'll tell you if it is a multiple of 10")
# number = int(number)
#
# if number == 0:
#     print(f"\n{number} is not a multiple of 10")
# elif number % 10 == 0:
#     print(f"\n{number} is a multiple of 10")
# else:
#     print(f"\n{number} is not a multiple of 10")

# prompt = "\nWhat toppings would you like on your pizza?"
# prompt += "\n(Enter 'quit' once you are finished adding toppings)"
#
# while True:
#     toppings = input(prompt)
#
#     if toppings == 'quit' or 'Quit':
#         break
#     else:
#         print(f"I'll add {toppings} to your pizza?")
#
# prompt = "\nHow old are you?"
# prompt += "\nEnter 'quit' to end the program"
#
# while input(prompt) == int():
#     age = input(prompt)
#
#     if age < 3:
#         print("Your ticket is free")
#     elif age < 12:
#         print("Your ticket is $10")
#     else:
#         print("Your ticket is $15")

# prompt = "\nHow old are you?"
# prompt += "\nEnter 'quit' to end the program"
#
# active = True
# while active:
#     age = input(prompt)
#
#     if age == 'quit':
#         break
#
#     age = int(age)
#     if age < 3:
#         print("Your ticket is free")
#     elif age < 12:
#         print("Your ticket is $10")
#     else:
#         print("Your ticket is $15")

# x=1
# while x < 10:
#     print("please stop this")

# sandwich_orders = ['pastrami','tuna','pastrami','beef','pastrami','corned beef','radish']
# finished_sandwiches=[]
#
# while 'pastrami' in sandwich_orders:
#     print('We are out of pastrami. Please pick another sandwich')
#     sandwich_orders.remove('pastrami')
#     sandwich_order_new = input("Which sandwich do you want?")
#     sandwich_orders.append(sandwich_order_new)
#
# while sandwich_orders:
#     in_progress_order = sandwich_orders.pop()
#
#     print(f"Making your {in_progress_order} sandwich")
#     finished_sandwiches.append(in_progress_order)
#
# print(f"\nThe following sandwiches have been made:")
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich.title())

responses = {}

polling_active = True

while polling_active:
    name = input(f"\nWhat is your name")
    response = input(f"\nWhat is your dream vacation?")

    responses[name] = response

    repeat = input("Would anyone else like to answer")
    if repeat == 'no':
        polling_active = False

print("\n---Poll Results---")
for name,response in responses.items():
    print(f"{name}'s dream vacation is {response}")
