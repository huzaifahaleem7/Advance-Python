import time 
import multiprocessing as mp


sqr_arr = []

def sqr_cal(arr):
    global sqr_arr
    for i in arr:
        time.sleep(0.2)
        sqr = i * i
        print(f"Square of {i} is {sqr}")
        sqr_arr.append(sqr)
        print(sqr_arr)


# def cube_cal(arr):
#     for i in arr:
#         time.sleep(0.2)
#         cube = i * i * i
#         print(f"Cube of {i} is {cube}")


if __name__ == "__main__":
    
    array = range(1, 10)
    
    t = time.time()
   
    t1 = mp.Process(target=sqr_cal, args=(array,))
    # t2 = mp.Process(target=cube_cal, args=(array,))
    
    t1.start()
    # t2.start()

    t1.join()
    # t2.join()
    
    print(sqr_arr)
    print(f"Total time without threading is {time.time() - t} seconds")