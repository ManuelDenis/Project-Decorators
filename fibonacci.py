def fibonacci():
    lis = [0, 1, 1]
    yield 0
    yield 1
    yield 1
    while lis[0] >= 0:
        lis[0] = lis[1]
        lis[1] = lis[2]
        lis[2] = lis[0] + lis[1]
        yield lis[2]






generator = fibonacci()
for x in range(7):
    print(next(generator))