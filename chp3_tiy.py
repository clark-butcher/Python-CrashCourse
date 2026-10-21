# #3-1names
# names = ['Filip','Tyler','Christian','Ed','Jon']
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
#
# #3-2Greetings
# print('Thanks for the card', names[0])
# print('Thanks for the card', names[1])
# print('Thanks for the card', names[2])
# print('Thanks for the card', names[3])
# print('Thanks for the card', names[4])

#3-3 Your Own List
# cars=['subaru','toyota','honda']
# print('I would like to own', cars[0], 'cars')
# print('I would like to own', cars[1], 'cars')
# print('I would like to own', cars[2], 'cars')

#3-4
guest_list = ['Lincoln','Einstein','Aristotle']
print(f"Would you like to come to dinner {guest_list[0]}?")
print(f"Would you like to come to dinner {guest_list[1]}?")
print(f"Would you like to come to dinner {guest_list[2]}?")

print(f"{guest_list[2]} is unable to make it")

guest_list.remove('Aristotle')
guest_list.append('Obama')
print(guest_list)
print(f"Would you like to come to dinner {guest_list[0]}?")
print(f"Would you like to come to dinner {guest_list[1]}?")
print(f"Would you like to come to dinner {guest_list[2]}?")

print(f"Hey {guest_list[0]}, {guest_list[1]}, and {guest_list[2]}, I found a bigger table")
guest_list.insert(0,"Ferdinand")
guest_list.insert(1,"Joan")
guest_list.append("Ignatious")
print(guest_list)

#3-7
print(f"Hey {guest_list}, I can only invite 2 of you)")
guest_list.pop(4)
guest_list.pop(3)
guest_list.pop(2)
guest_list.pop(2)
print(guest_list)

print(f"Hey {guest_list[0]} and {guest_list[1]} you can still come")

del guest_list[0]
del guest_list[0]
print(guest_list)