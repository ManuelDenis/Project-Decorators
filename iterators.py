def multiply(times):
    def decorator(function):
        def wrapper(number):
            res = function(number) * times
            return res
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number


print(add_ten(3))
