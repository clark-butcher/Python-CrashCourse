# Person_1 = {'Name':'Johnny','Hair':'brown','job':'Production'}
#
# print(Person_1['Name'])
# print(Person_1['Hair'])
# print(Person_1['job'])
#
# favorite_numbers = {'john':'5','Catherine':'17','Sean':'14','Brian':'42','Kong':'12'}
#
# print(favorite_numbers['john'])
# print(favorite_numbers['Catherine'])
# print(favorite_numbers['Sean'])
# print(favorite_numbers['Brian'])
# print(favorite_numbers['Kong'])
# from Chp6_favorite_languages import favorite_languages

# programming_word = {'key':'term that connects to a value','list':'stores data', 'dictionary':'reference for data','set':'collection in which each item must be unique'}
# #
# # print('key')
# # print(programming_word['key'])
# #
# # print('\nlist')
# # print(programming_word['list'])
#
# for key, value in programming_word.items():
#     print(f"{key.title()} is a {value}")

# rivers = {'nile':'egypt','amazon':'brazil','seine':'france'}
#
# for key, value in rivers.items():
#     print(f"The {key.title()} runs through {value.title()}")
#
# for key in rivers.keys():
#     print(key.title())
#
# for value in rivers.values():
#     print(value.title())

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'}

favorite_language_polls = ['jen','sarah', 'brian', 'tommy']

for key, value in favorite_languages.items():
    if key in favorite_language_polls:
        print(f"{key.title()}, thank you for taking the poll. I like {value.title()} too")
    elif key not in favorite_language_polls:
        print(f"{key.title()}, please take our poll")
for poll in favorite_language_polls:
    if poll not in favorite_languages.keys():
        print(f"Thanks for taking the poll,{poll.title()}. What's your favorite language?")