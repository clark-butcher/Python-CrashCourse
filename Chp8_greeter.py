# def greet_user(username):
#     """Display a simple greeting."""
#     print(f"Hello, {username.title()}!")
#
# greet_user('jesse')
# greet_user('todd')

def get_formatted_name(first_name,last_name):
    """Return a full name, neatly formatted."""
    full_name = (f"{first_name.title()} {last_name.title()}")
    return full_name.title()

while True:
    print("Please tell me your name")
    print("Enter 'q' to quit at any time")
    f_name = input("What is your first name?")
    if f_name == 'q':
        break
    l_name = input("What is your last name?")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name,l_name)
    print(f"Hello,{formatted_name}")