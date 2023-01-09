def make_bold(function):
    def wrapper(*arg):
        res = function(*arg)
        return f"<b>{res}</b>"
    return wrapper


def make_italic(function):
    def wrapper(*arg):
        res = function(*arg)
        return f"<i>{res}</i>"
    return wrapper


def make_underline(function):
    def wrapper(*arg):
        res = function(*arg)
        return f"<u>{res}</u>"
    return wrapper


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))