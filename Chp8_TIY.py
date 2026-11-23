# def display_message(learnings):
#     print(f"Today I learned {learnings}!")
# display_message('how to do dictionaries')
# display_message('how to deal with loops')
#
# def favorite_book(book):
#     print(f"One of my favorite books is {book.title()}")
# favorite_book('Don Quixote')
from pydoc import describe


# def make_shirt(size,text):
#     print(f"You have requested a {size} shirt with '{text}' on the front of it.")
# make_shirt('Large','This is my shirt')
# make_shirt(size='Medium',text='This is not my shirt')

# def make_shirt(size='large',text='I love Python'):
#     print(f"You have requested a {size} shirt with '{text}' on the front of it.")
# make_shirt()
# make_shirt(size='medium',text='I Love C++')
#
# def describe_city(city,country='Spain'):
#     print(f"\n{city.title()} is in {country.title()}")
# describe_city('cordoba')
# describe_city('granada')
# describe_city('lisbon',country='Portugal')

# def city_country(cityname,countryname):
#     print(f'"{cityname.title()}, {countryname.title()}"')
# city_country('santiago','chile')
# city_country('Rio','Brazil')
# city_country('paris','france')

# def make_album(artist,album_title,song_number=None):
#     album = {'artist':artist,'album title':album_title}
#     if song_number:
#         album['song_number']=song_number
#     return album
# info = make_album('Strokes','Is This It',song_number=10)
# print(info)
# info = make_album('Joy Division','Disorder',song_number=11)
# print(info)
# info = make_album('Beatles','Let It Be')
# print(info)

def make_album(artist,album_title,song_number=None):
    album = {'artist':artist,'album title':album_title}
    return album

while True:
    artist = input("Who made the album?")
    album_title = input("What is the title of the album?")
    info = make_album(artist, album_title)
    print(info)
