def weight_calculate():
    while True:
        input_option = input('''
Please type in the preferred weight unit:
Kg
Lbs
''').lower()
        print('Enter the weight:')
        weight = input()

        try:
             weight = float(weight)

        except:
             print("FAILED: Enter weight using numeric digits")
             continue

        if input_option == 'kg':
            print(round(weight * 2.2046, 2))
        elif input_option == 'lbs':
            print(round(weight / 2.2046, 2))
        else: "invalid conversion"            
        break

weight_calculate()