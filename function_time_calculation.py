import time

def tictoc(func):
    """
    Returns the amount of time taken to run a function.
    
    Param: 
          func -> Takes function as an input.
    """
    def wrapper():
        t1=time.time()
        func()
        t2=time.time()-t1
        print(f"{func.__name__} ran for {t2} seconds")
    return wrapper

@tictoc
def func1():
    time.sleep(1.2)

@tictoc
def func2():
    time.sleep(.4)

func1()
func2()
print("All done")