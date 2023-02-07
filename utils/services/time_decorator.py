import math
import time


def time_function(function):
    def new_function(*args, **kwargs):
        start = time.time()
        value = function(*args, **kwargs)
        end = time.time()
        difference = end - start
        print("Time --> ", str(round(difference,2)) , " seconds")
        return value
    return new_function
