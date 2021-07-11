class employe():
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print(self.id,self.name)

emp1=employe(2004,"madesh")
emp2=employe(2005,"pavis")
emp1.display()
emp2.display()