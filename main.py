class car:
    def __init__(self,modelname,year):
        self.modelname = modelname
        self.year=year
    def display(self):
        print(self.modelname,self.year)


c1 = car("RR",2015)
c2 = car("Mercides",2018)
c3 = car("BMW",2018)
c4 = car("Defender",2015)
c5 = car("Gwagon",2020)

c1.display()
c4.display()

# Multilevel Inheritance 
class GrandFather:
    def cough(self):
        print("GrandFather is coughing")

class Father(GrandFather):
    def speak(self):
        print("Father is Speaking")
class Son(Father):
    def listen(self):
        print("Son is Listening")

beta = Son()
beta.speak()
beta.listen()