import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        finish = time.perf_counter()
        print("Function time: ", (finish - start))
        return result
    return wrapper


def debug_log_function(func):
    def wrapper(*args, **kwargs):
        print("Debug Log: ", func)
        return func(*args, **kwargs)
    return wrapper