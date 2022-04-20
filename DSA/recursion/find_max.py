# def find_max(arr):
#     if len(arr) < 3:
#         if arr[0] > arr[1]:
#             return arr[0]
#         else:
#             return arr[1]
#     max = find_max(arr[1:])
#     print(max)
#     return max

def find_max(arr):
    
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0] 
        else:
            return arr[1]
    sub_max = find_max(arr[1:])
    print(arr)
    return arr[0] if arr[0] > sub_max else sub_max
    
    return sub_max

if __name__ == "__main__":
    print(find_max([1, 4, 13, 2, 5]))



# [4, 2] => Base Case Hit: Pop stack  pop1: 4
# [1, 4, 2]
# [13, 1, 4, 2]
