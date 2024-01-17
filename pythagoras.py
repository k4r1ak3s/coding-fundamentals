from math import sqrt

def calculate():
    input_option = input('''
Please type in the math operation you would like to complete:
A: Calculate the length of side A using the length of sides B and C.
B: Calculate the length of side B using the length of sides A and C.
C: Calculate the length of side C using the length of sides A and B.
''')
    
    if input_option == 'A':
        side_b = int(input('Please enter the legnth of side B: '))
        side_c = int(input('Please enter the legnth of side C: '))
        print(f"The length of side A is: {round(sqrt(side_b ** 2 + side_c ** 2),2)}")
    
    elif input_option == 'B':
        side_a = int(input('Please enter the legnth of side A: '))
        side_c = int(input('Please enter the legnth of side C: '))
        print(f"The length of side B is: {round(sqrt(side_a ** 2 + side_c ** 2),2)}")
    
    elif input_option == 'C':
        side_a = int(input('Please enter the legnth of side A: '))
        side_b = int(input('Please enter the legnth of side B: '))
        print(f"The length of side C is: {round(sqrt(side_a ** 2 + side_b ** 2),2)}")
    
    else: print("invalid number")

calculate()