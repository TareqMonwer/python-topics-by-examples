def foo():
    x = 1
    yield x
    x += 1
    yield x
    x += 2
    yield x


if __name__ == '__main__':
    #for item in foo():
        #print(item)
    y = foo()
    print(next(y))
    print(next(y))
    print(next(y))
    print(next(y))

