subjects = ['Math', 'English', 'IT']
final_average={}
for subject in subjects:
    num_1 = float(input(f"Input grade 1 for {subject}: "))
    num_2 = float(input(f"Input grade 2 for {subject}: "))
    num_3 = float(input(f"Input grade 3 for {subject}: "))

    average = (num_1 + num_2 + num_3) / 3

    if average >= 65:
        print(f"The Average grade for {subject} is {round(average, 2)} - Pass")

    elif average <= 64:
        print(f"The Average grade for {subject} is {round(average, 2)} - Fail")
    
    final_average[subject] = (round(average, 2))

    print(final_average)
    

    