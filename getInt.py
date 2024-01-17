min = 1
max = 100
counter = 1

while True:
    counter +=1
    inputs = int(input(f"Enter a number between {min} and {max}: "))
    if min <= inputs <= max:
        print(f"The number {inputs} is between {min} and {max}.")
        break
    if counter <= 3:
        print(f"Please enter a value between {min} and {max}.")
    else: 
        print(f"You've had 3 chances. Terminating.")
        break
