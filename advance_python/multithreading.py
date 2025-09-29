import time 
import threading

def sqr_cal(arr):
    for i in arr:
        time.sleep(0.2)
        sqr = i * i
        print(f"Square of {i} is {sqr}")

def cube_cal(arr):
    for i in arr:
        time.sleep(0.2)
        cube = i * i * i
        print(f"Cube of {i} is {cube}")


if __name__ == "__main__":
    
    array = range(1, 10)
    
    t = time.time()
    # sqr_cal(array)
    # cube_cal(array)
    t1 = threading.Thread(target=sqr_cal, args=(array,))
    t2 = threading.Thread(target=cube_cal, args=(array,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    print(f"Total time without threading is {time.time() - t} seconds")