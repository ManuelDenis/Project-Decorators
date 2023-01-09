def type_check(typ):
    def decorator(function):
        def wrapper(arg):
            if isinstance(arg, typ):
                return function(arg)
            else:
                return "Bad Type"
        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))