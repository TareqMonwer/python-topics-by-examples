def getsum(arr):
    if len(arr) < 2:
        return arr[0]
    return arr[0] + getsum(arr[1:])


if __name__ == "__main__":
    print(getsum([1,2,3,4]))