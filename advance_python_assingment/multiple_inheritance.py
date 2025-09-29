# Create multiple inheritance on teacher,student and youtuber.
# Q. if we have created teacher and now one student joins master degree with becoming teacher then what??

# Ans :  just make subclass from  teacher so that student will become teacher
# Now student is teacher as well as youtuber then what???
# -just use multiple inheritance for these three relations

class Teacher:
    def teachers_action(self):
        print("I can teach")


class Engineer:
    def Engineers_action(self):
        print("I can code")


class Youtuber:
    def youtubers_action(self):
        print("I can code and teach")


class Person(Teacher, Engineer, Youtuber):
    pass


coder = Person()
coder.teachers_action()
coder.Engineers_action()
coder.youtubers_action()