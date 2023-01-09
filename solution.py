def logged(function):
    def wrapper(*args):
        res = function(*args)
        return f"you called {function.__name__}{args}\nit returned {res}"

    return wrapper


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
