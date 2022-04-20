def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    print(less, '<less', pivot, '<pivot', greater, '<great')
    return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == "__main__":
    print(quicksort([43, 39, 29, 22, 35]))

    # arr: [39, 29, 22, 35], piv: 43, less: [39, 29, 22, 35], greater: []
    # arr: [29, 22, 35], piv: 39, less: [29, 22, 35], greater: []
    # arr: [22, 35], piv: 29, less: [22], greater: [35]
    # BASECASE HIT
    # stack: (less pivot greater)
    # 22, 29, 35
    # 22, 29, 35, 39
    # 22, 29, 35, 39, 43