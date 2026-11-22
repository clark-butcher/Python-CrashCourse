# def display_message(learnings):
#     print(f"Today I learned {learnings}!")
# display_message('how to do dictionaries')
# display_message('how to deal with loops')
#
# def favorite_book(book):
#     print(f"One of my favorite books is {book.title()}")
# favorite_book('Don Quixote')

# def make_shirt(size,text):
#     print(f"You have requested a {size} shirt with '{text}' on the front of it.")
# make_shirt('Large','This is my shirt')
# make_shirt(size='Medium',text='This is not my shirt')

# def make_shirt(size='large',text='I love Python'):
#     print(f"You have requested a {size} shirt with '{text}' on the front of it.")
# make_shirt()
# make_shirt(size='medium',text='I Love C++')

def describe_city(city,country='Spain'):
    print(f"\n{city.title()} is in {country.title()}")
describe_city('cordoba')
describe_city('granada')
describe_city('lisbon',country='Portugal')
