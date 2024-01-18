def make_pizza(size, *toppings, final_message, **sides):
    print(f"order for {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")
    print("with the sides: ")
    print(" - " + sides["side"])
    print(" - " + sides["meat_side"])
    print(final_message)
    

make_pizza(12, "extra cheese", "mushrooms", "green peppers", side = "fries", meat_side = "chicken dippers", final_message = "Thanks for your order!!")