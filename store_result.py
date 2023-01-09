class store_results:
    counter = 0

    def __init__(self, function):
        self.function = function

    def __call__(self, *args):
        file = open("results", "a")
        self.function(*args)
        text = f"Result {store_results.counter}. Function '{self.function.__name__}' was called. Argument is {', '.join([str(x) for x in args])} Result: {self.function(*args)}"
        file.write(text + '\n')
        file.close()
        store_results.counter += 1
        return text


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b, c):
    return a * b * c


add(2, 2)
mult(6, 4, 7)
