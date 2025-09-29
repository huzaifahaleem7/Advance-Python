# Create a custom exception AdultException.

# Create a class Person with attributes name and age in it.

# Create a function get_minor_age() in the class. It throws an exception if the person is adult otherwise returns age.

# Create a function display_person() which prints the age and name of a person.

# let us say,

# if age>18 
#     he is major
# else
#     raise exception

# create cusomException named ismajor and raise it if age<18.

class AdultException(Exception):
    pass


class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        

    def get_minor_age(self):
        if int(self.age) > 18:
            raise AdultException("Person is an adult.")
        else:
            return self.age
    def display_person(self):
        try:
            age = self.get_minor_age()
            print(f"Name: {self.name}, Age: {age}")
        except AdultException as e:
            print(f"AdultException: {e}")
        finally:
            print(f"Name: {self.name}")

if __name__ == "__main__":
    p1 = Person(17, "Huzaifa")
    p1.display_person()
    
    p2 = Person(26, "Hanzla")
    p2.display_person()
            
    