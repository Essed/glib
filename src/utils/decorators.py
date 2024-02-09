import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start= time.time()
        result = func(*args, **kwargs)
        print("Function time: ", time.time() -start)
        return result
    return wrapper


def debug_log_function(func):
    def wrapper(*args, **kwargs):
        print("Debug Log: ", func)
        return func(*args, **kwargs)
    return wrapper