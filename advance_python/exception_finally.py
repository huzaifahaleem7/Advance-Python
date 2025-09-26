class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
        
    def print_error(self):
        print(self.msg)


try:
    raise MyError("Something went wrong")
except MyError as e:
    e.print_error()
finally:
    print("Program finished")


# try:
#     raise MemoryError("memory error")
# except MemoryError as e:
#     print(e)
