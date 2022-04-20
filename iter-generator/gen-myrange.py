def myrange(n):
    x = 0
    while x < n:
        yield x
        x += 1


if __name__ == '__main__':
    for i in myrange(10):
        print(i)

