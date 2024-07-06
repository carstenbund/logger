import time
from functools import wraps
from contextlib import contextmanager
from MYLogger import Logger

logger = Logger()

def time_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        log.log(f"[{func.__name__}] Elapsed time: {elapsed_time:.4f} seconds")
        return result
    return wrapper

@contextmanager
def time_step(name):
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        elapsed_time = end_time - start_time
        log.log(f"[{name}] Elapsed time: {elapsed_time:.4f} seconds")
        
