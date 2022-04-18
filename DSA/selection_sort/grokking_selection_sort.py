def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    arr_len = len(arr)
    for i in range(1, arr_len):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    sorted_arr = list()
    arr_len = len(arr)
    for i in range(arr_len):
        smallest_index = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest_index))
    return sorted_arr


if __name__ == "__main__":
    arr = [33, 4, 3, 11, 2, 5, 10, 11]
    print(selection_sort(arr))
