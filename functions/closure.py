def addition(n):
    def add(cl_n):
        return n + cl_n
    return add


if __name__ == '__main__':
    one_plus = addition(1)
    print(one_plus(10))
    print(one_plus.__closure__)
    print(addition.__closure__)

