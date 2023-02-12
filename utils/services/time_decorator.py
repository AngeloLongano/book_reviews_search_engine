from time import time, gmtime, strftime


def time_function(function):
    """

    :param function: 
    :return function:
    
    Decoratore per il calcolo del tempo di esecuzione della funzione
    """
    def new_function(*args, **kwargs):
        start = time()
        value = function(*args, **kwargs)
        end = time()
        difference = end - start
        print(function.__name__, ": execution time ", str(round(difference, 2)), " seconds")
        return value

    return new_function


def long_time_function(function):
    """

    :param function: 
    :return function:
    
    Decoratore per il calcolo del tempo di esecuzione di funzioni più lunghe
    """
    def new_function(*args, **kwargs):
        start = time()
        value = function(*args, **kwargs)
        end = time()

        difference = strftime("%H hours %M minutes %S seconds", gmtime(end - start))
        print(function.__name__, ": execution time ", difference)
        return value

    return new_function
