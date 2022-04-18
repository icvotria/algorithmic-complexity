def countingSort(arr):
    count_arr = []
    x = 0
    arr_size = max(arr) + 1
    count_arr.extend([x]*(arr_size))
    
    for i in arr:
        count_arr[i] += 1
    print(count_arr)

countingSort([3, 4, 2, 2, 1, 10])