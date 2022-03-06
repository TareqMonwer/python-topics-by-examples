class my_range:
    def __init__(self, n, max_n=None, step=1):
        self.index = n
        self.max_index = max_n if max_n else n - 1
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= self.max_index:
            self.index += self.step
            return self.index - self.step
        else:
            raise StopIteration()


if __name__ == "__main__":
    for i in my_range(1, 11, 3):
        print(i)

