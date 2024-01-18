# data held in dictionaries within the class
#class Students:
#    pass

#student1 = Students()
#student2 = Students()

# setting attributes outside the class if not within the class
#student1.first = "john"
#student1.last = "smith"
#student1.age = 10

'''class Student:
    def __init__(self, first, last, age): # __<>__ indicates a background task, init will initialise with args.... self refers to the object and the rest are args, self can be named anythin
        self.first = first # init method initialises object mapping to attributes.
        self.last = last # self maps class data to the object
        self.age = age

student1 = Student("john", "smith", 10)
student2 = Student("katie", "smith", 12)

print(student1.age, student2.age)'''


'''class Student:
    def __init__(self, first, last, age): # __<>__ indicates a background task, init will initialise with args.... self refers to the object and the rest are args, self can be named anythin
        self.first = first # init method initialises object mapping to attributes.
        self.last = last # self maps class data to the object
        self.age = age
        self.full = first + ' ' + last

student1 = Student("john", "smith", 10)
student2 = Student("katie", "smith", 12)

print(student1.full)'''


# as method
'''class Student:
    def __init__(self, first, last, age): # __<>__ indicates a background task, init will initialise with args.... self refers to the object and the rest are args, self can be named anythin
        self.first = first # init method initialises object mapping to attributes.
        self.last = last # self maps class data to the object
        self.age = age
        #self.full = first + ' ' + last

    def full_name(self):
        return(self.first + ' ' + self.last)

student1 = Student("john", "smith", 10)
student2 = Student("katie", "smith", 12)

print(student1.full_name())
print(Student.full_name(student2))'''

# method that adds to age
'''class Student:
    def __init__(self, first, last, age): # __<>__ indicates a background task, init will initialise with args.... self refers to the object and the rest are args, self can be named anythin
        self.first = first # init method initialises object mapping to attributes.
        self.last = last # self maps class data to the object
        self.age = age

    def full_name(self):
        return(self.first + ' ' + self.last)
    
    def change_age(self):
        self.age = int(self.age + 1)

student1 = Student("john", "smith", 10)
student2 = Student("katie", "smith", 12)

print(student1.age, student2.age)
student1.change_age()
student2.change_age()
print(student1.age, student2.age)'''

# self class variable
'''class Student:
    age_increase_amount = 25

    def __init__(self, first, last, age): # __<>__ indicates a background task, init will initialise with args.... self refers to the object and the rest are args, self can be named anythin
        self.first = first # init method initialises object mapping to attributes.
        self.last = last # self maps class data to the object
        self.age = age

    def full_name(self):
        return(self.first + ' ' + self.last)
    
    def change_age(self):
        self.age = int(self.age + self.age_increase_amount)

student1 = Student("john", "smith", 10)
student2 = Student("katie", "smith", 12)

print(student1.age, student2.age)
student1.change_age()
student2.change_age()
print(student1.age, student2.age)'''

# __dict__ shows each object as dict
'''class Student:
    age_increase_amount = 25

    def __init__(self, first, last, age): # __<>__ indicates a background task, init will initialise with args.... self refers to the object and the rest are args, self can be named anythin
        self.first = first # init method initialises object mapping to attributes.
        self.last = last # self maps class data to the object
        self.age = age

    def full_name(self):
        return(self.first + ' ' + self.last)
    
    def change_age(self):
        self.age = int(self.age + self.age_increase_amount)

student1 = Student("john", "smith", 10)
student2 = Student("katie", "smith", 12)

print(student1.__dict__)
print(student2.__dict__)
student1.change_age()
student2.change_age()
print(student1.__dict__)
print(student2.__dict__)

# change the variable within the class for all
Student.age_increase_amount = 20
print(Student.__dict__)
# change the variable within the class for certain objects
student1.age_increase_amount = 10
student1.change_age()
print(student1.age)
print(student1.__dict__)
print(student2.__dict__)'''

# non self class variable

'''class Student:
    age_increase_amount = 25
    num_of_students = 0

    def __init__(self, first, last, age): # __<>__ indicates a background task, init will initialise with args.... self refers to the object and the rest are args, self can be named anythin
        self.first = first # init method initialises object mapping to attributes.
        self.last = last # self maps class data to the object
        self.age = age

        Student.num_of_students += 1

    def full_name(self):
        return(self.first + ' ' + self.last)
    
    def change_age(self):
        self.age = int(self.age + self.age_increase_amount)

print(Student.num_of_students)
student1 = Student("john", "smith", 10)
student2 = Student("katie", "smith", 12)

print(Student.num_of_students)'''

# parent and child classes, inheritance
'''class Animal:
    def __init__(self, name, species): 
        self.name = name 
        self.species = species

    def eat(self):
        print(f"{self.name} is eating")

class Cat(Animal):
    def __init__(self, name, species, breed): 
        super().__init__(name, species)
        self.breed = breed

    def meow(self):
        print("meow")

my_cat = Cat("w", "f", "g")

my_cat.meow()
my_cat.eat()'''

# string method with inheritance
class Animal:
    def __init__(self, name, species): 
        self.name = name 
        self.species = species

    def eat(self):
        print(f"{self.name} is eating")

    def __str__(self):
        return(f"{self.name} {self.species}")

class Cat(Animal):
    def __init__(self, name, species, breed): 
        super().__init__(name, species)
        self.breed = breed

    def meow(self):
        print("meow")

    def __str__(self):
        return(f"{self.name}, {self.species}, {self.breed}")

my_cat = Cat("w", "x", "y")
print(my_cat)

