import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken by {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

@timer
def slow_function(n):
    time.sleep(n)

slow_function(3)
