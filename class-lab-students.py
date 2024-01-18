class Students:
    def __init__(self, first, last, age, student_classroom): # __<>__ indicates a background task, init will initialise with args.... self refers to the object and the rest are args, self can be named anythin
        self.first = first # init method initialises object mapping to attributes.
        self.last = last # self maps class data to the object
        self.age = age
        self.student_classroom = student_classroom

    def classroom(self):
        return self.student_classroom
    
    def score_average(self, score1, score2, score3):
        average = (score1 + score2 + score3) / 3
        print(f"The average score for {self.first + ' ' + self.last} is {average}")

student1 = Students("john", "smith", 10, "2F")
student2 = Students("katie", "smith", 12, "5B")

print(student2.score_average(88, 56, 63))