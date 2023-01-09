import time
from datetime import datetime


def exec_time(function):
    def wrapper(*args):
        start = datetime.now()
        function(*args)
        end = datetime.now()
        delta = end - start
        return delta.total_seconds()
    return wrapper


@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1
print(loop())