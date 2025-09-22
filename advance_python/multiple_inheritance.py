class Father:
    def skills(self):
        print("programming")

class Mother:
    def skills(self):
        print("cooking")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("sports")
        
obj = Child()
obj.skills()