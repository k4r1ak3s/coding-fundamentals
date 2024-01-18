#def addition(num_1, num_2):
#    return num_1 + num_2

#print(addition(1, 2))


#def fruit_list(*fruits):
#    print("the fruits are: ")
#    for fruit in fruits:
#        print(fruit)

#fruit_list("apple", "orange", "pear")

############ *args #############################

#def make_pizza(size, *toppings):
#    print(f"order for {size}-inch pizza with the following toppings:")
#    for topping in toppings:
#        print(f" - {topping}")

#make_pizza(12, "extra cheese", "mushrooms", "green peppers")

################ kwargs

#def fruit_list(fruit1, fruit2, fruit3):
#   print(f"fav fruit = {fruit1}")
#    print(f"2nd fav = {fruit2}")
#    print(f"3rd fav = {fruit3}")

fruit_list(fruit1 = "apple", fruit3 = "pear", fruit2 = "orange")


######################## **kwargs

#def fav_food(**food):
#    print("fav food is", food["fruit"], "not", food["dessert"])

#fav_food(dessert = "ice-cream", fruit = "apple", dairy = "cheese")

####### passing list as arg

#def my_function(food):
#    for x in food:
#        print(x)

#list1 = ["apple", "pear", "orange"]
#my_function(list1)