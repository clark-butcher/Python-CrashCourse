requested_toppings = ['mushrooms','extra cheese']
# if requested_toppings != 'Anchioves':
#     print("Hold the anchioves")
#
# age = 18
# print(age == 18)

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
requested_toppings.append('pepperoni')
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
requested_toppings.remove('extra cheese')
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

