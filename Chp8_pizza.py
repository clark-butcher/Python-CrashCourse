def make_pizza(size, *toppings):
    print(f"The following pizza with a size of {size} inches have been made:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms','green peppers','extra cheese')
