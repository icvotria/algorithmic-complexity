def countingSort(arr):
    result = []
    x = 0
    arr_size = max(arr) + 1
    result.extend([x]*(arr_size))
    
    for i in arr:
        result[i] += 1
    print(result)

countingSort([3, 4, 2, 2, 1, 10])