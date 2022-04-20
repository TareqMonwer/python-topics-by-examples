def counter(arr):
    if not arr:
        return 0
    return 1 + counter(arr[1:])


if __name__ == "__main__":
    print(counter([1,3,1,4,4]))