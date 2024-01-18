class Bird:
    _number_of_birds = 0
    def __init__(self): # __<>__ indicates a background task.
        #self.extinct = first # init method initializes the object with these attributes.

        Bird._number_of_birds += 1

    def speak(self):
        pass
    
class Owl(Bird):
    def speak(self):
        return("Twit Twoooooooo")
    

class Dodo(Bird):
    def speak(self):
        return("Bwwwwwwwww (like a pigeon apparently)")

owl = Owl()
dodo = Dodo()
print(f"There are {Bird._number_of_birds} in this aviary!")
input_option = input('''
Please select which bird you woul like to make a noise:
1: Owl
2: Dodo
''')

if input_option == '1':
    print(owl.speak())
elif input == '2':
    print(dodo.speak())
else: pass
                         
