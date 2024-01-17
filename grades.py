def level_and_grade():
    level = int(input('''
Please enter the number corresponding with level of study
Level 1: 1
Level 2: 2
'''))
    grade = int(input('Please enter the grade: '))

    if level == 1:
        if grade >= 71:
            print("Distinction")
        elif grade >= 61:
            print("Merit")
        elif grade >= 50:
            print("Pass")
        else: print("Fail")
    
    if level == 2:
        if grade >= 66:
            print("Distinction")
        elif grade >= 51:
            print("Merit")
        elif grade >= 40:
            print("Pass")
        else: print("Fail")

level_and_grade()