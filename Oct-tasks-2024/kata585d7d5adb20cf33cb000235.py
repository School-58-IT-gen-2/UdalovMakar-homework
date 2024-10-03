def find_uniq(arr):
    if arr.count(arr[0]) == 1: return arr[0]
    for i in arr:
        if i != arr[0]:
            return i