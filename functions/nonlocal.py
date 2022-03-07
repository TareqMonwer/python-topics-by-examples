def addition(n1, n2):
    result = 0

    def add():
        nonlocal result
        result = n1 + n2
        print("Result printing from add(): ", result)
    add()
    print("Result from addition: ", result)


if __name__ == "__main__":
    addition(10, 20)

