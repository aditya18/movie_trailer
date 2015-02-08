class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent called")
        self.lastname = last_name
        self.eyecolor = eye_color

    def show_info(self):
        print("Last Name = "+self.lastname)
        print("Eye Color ="+self.eyecolor)
        

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name = "+self.lastname)
        print("Eye = "+self.eyecolor)
        print("Toys = "+str(self.number_of_toys))
               
              

billy = Parent("Adi", "blue")
billy.show_info()

rao = Child("Rao", "red", 5)
rao.show_info()


#print(rao.lastname)
#print(rao.number_of_toys)

