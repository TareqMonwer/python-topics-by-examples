def binary_search(arr, left, right, item):
    if left > right:
        return -1

    mid = (left + right) // 2
    if item == arr[mid]:
        return mid

    if item < arr[mid]:
        return binary_search(arr, left, right-1, item)
    return binary_search(arr, mid+1, right, item)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(arr, 0, len(arr)-1, 9))
