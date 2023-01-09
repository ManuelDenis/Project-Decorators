def even_parameters(function):
    def wrapper(*args):
        sit = True
        for x in args:
            if not isinstance(x, int):
                sit = False
                break
            if x % 2 != 0:
                sit = False
                break
        if sit:
            res = function(*args)
            return res
        else:
            return f"Please use only even numbers!"
    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8, '4'))
print(multiply(2, 4, 9, 8))
