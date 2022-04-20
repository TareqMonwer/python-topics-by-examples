def merge(arr, start, mid, end):
    temp_arr = []
    ...    


def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)