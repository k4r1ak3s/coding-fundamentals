
while True:
    milkshake_options = input('''
                              
Barman: What milkshake would you like?
1. Chocolate
2. Strawberry
3. Vanilla
________________________________________
Q. Quit                             
''')
    
    milkshake_dict = {"chocolate": 11, "stawberry": 4, "vanilla": 3}
    budget = 10

    if milkshake_options == '1':
        print("Sam: I would like Chocolate please :)")
        new_budget = budget - milkshake_dict['chocolate']


    elif milkshake_options == '2':
        print("Sam: I would like Strawberry please :)")
        new_budget = budget - milkshake_dict['stawberry']


    elif milkshake_options == '3':
        print("Sam: I would like Vanilla please :)")
        new_budget = budget - milkshake_dict['vanilla']

    elif milkshake_options == 'Q':
        print("Barman: OK! Good luck on your search for love (you'll need it)")
        break

    if new_budget > 0:
        print(f"Barman: the cost is {milkshake_dict['chocolate']}, so your change is {new_budget}")
    elif new_budget < 0:
        print("How dare you! That is not enough! Get out my shop, you're barred.")
        break




