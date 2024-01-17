students=[]
for name in range(5):
    x=input("Enter name of students: ")
    students.append(x)

    if len(students) == 5:
        print(f"{students} is aweseome")