class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def intoduce(self):
        print('Name :', self.name,'age :',self.age,'gender :', self.gender)  

intro = Person("Peter",20,"Male")
intro.intoduce()