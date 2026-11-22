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
#
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'}
#
# favorite_language_polls = ['jen','sarah', 'brian', 'tommy']
#
# for key, value in favorite_languages.items():
#     if key in favorite_language_polls:
#         print(f"{key.title()}, thank you for taking the poll. I like {value.title()} too")
#     elif key not in favorite_language_polls:
#         print(f"{key.title()}, please take our poll")
# for poll in favorite_language_polls:
#     if poll not in favorite_languages.keys():
#         print(f"Thanks for taking the poll,{poll.title()}. What's your favorite language?")
#
# Person_1 = {'Name':'Johnny','Hair':'brown','job':'Production'}
# Person_2 = {'Name':'Tommy','Hair':'black','job':'Test'}
# Person_3 = {'Name':'Carl','Hair':'Blond','job':'PM'}
#
# people = [Person_1,Person_2,Person_3]
#
# for person in people:
#     for key, value in person.items():
#         print(f"\n{key}:{value}")
#
# dog = {'bonnie':'mary'}
# cat = {'Fluff':'Carl'}
# fish = {'spud':'Jon'}
#
# pets = [dog, cat, fish]
#
# for pet in pets:
#     for key, value in pet.items():
#         print(f"Hey {key}, is your owner {value}?")
#
# favorite_places = {
#     'jon': ['Rio','Chico'],
#     'earl': ['Cordoba','grenada'],
#     'phil': ['Worclaw'],
#     }
#
# for friend, places in favorite_places.items():
#     print(f"{friend.title()}'s favorite places are:")
#     for place in places:
#         print(f"\t{place.title()}")
#
# favorite_numbers = {
#     'john':['5','2'],
#     'Catherine':['17','3'],
#     'Sean':['14','13'],
#     'Brian':['42','25'],
#     'Kong':['18','12']
#     }
#
# for name, numbers in favorite_numbers.items():
#     print(f"{name.title()}'s favorite numbers are:")
#     for number in numbers:
#         print(f"{number}")

cities = {
    'prague':{
        'country':'czechia',
        'population':'1 million',
        'fact':'Great Christmas Markets',
        },
    'columbus':{
        'country':'united states',
        'population':'2 million',
        'fact':'Has Ohio State University',
        },
    'mexico city':{
        'country':'mexico',
        'population':'8 million',
        'fact':'Former site of aztec capital',
        },
    }

for city, cityinfo in cities.items():
    print(f"City Name: {city.title()}")
    country = cityinfo['country']
    population = cityinfo['population']
    fact = cityinfo['fact']

    print(f"{city.title()} is a city in {country.title()}, has a population on {population}, and fun fact:{fact}")