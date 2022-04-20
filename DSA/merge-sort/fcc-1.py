def split(arr):
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return left, right


def merge(left_arr, right_arr):
    temp = list()
    i, j = 0, 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            temp.append(left_arr[i])
            i += 1
        else:
            temp.append(right_arr[j])
            j += 1
    
    while i < len(left_arr):
        temp.append(left_arr[i])
        i += 1
    
    while j < len(right_arr):
        temp.append(right_arr[j])
        j += 1

    return temp


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left_subarr, right_subarr = split(arr)
    left = merge_sort(left_subarr)
    right = merge_sort(right_subarr)

    return merge(left, right)


def verify_sorted(arr):
    arr_len = len(arr)

    if arr_len == 0 or arr_len == 1:
        return True

    return arr[0] < arr[1] and verify_sorted(arr[1:])


if __name__ == "__main__":
    arr = [43, 65, 11, 4, 33]
    sorted = merge_sort(arr)
    print('sorted ', sorted)
    print("verified sort: ", verify_sorted(sorted))
