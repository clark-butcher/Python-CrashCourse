number = input("Give me a number. I'll tell you if it is even or odd")
number = int(number)

if number == 0:
    print(f"\nThis is a tough one. Ask a professor")
elif number % 2 == 0:
    print(f"\nThis number is even")
else:
    print(f"\nThis number is odd")