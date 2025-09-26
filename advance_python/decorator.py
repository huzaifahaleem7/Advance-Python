import time 
def time_cal(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        
        print(f"Total time to complete function is {(end - start) * 1000} mili second")

    return wrapper

@time_cal
def sqr_cal(a):
    sqr = [i*i for i in a]
  
@time_cal    
def cube_cal(a):
    cube = [i*i*i for i in a]
    
if __name__ == "__main__":
    array = range(1, 1000)
    sqr_cal(array)
    cube_cal(array)