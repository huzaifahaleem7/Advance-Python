class Myiterator():
    def __init__(self):
        self.channel = ["cnn", "bbc", "espn"]
        self.index = -1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index == len(self.channel):
            raise StopIteration
        
        return self.channel[self.index]
    
obj = Myiterator()
itr = iter(obj)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))