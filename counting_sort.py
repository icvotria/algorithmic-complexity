def countingSort(arr):
    arr_size = max(arr) + 1
    count_arr = [0]*arr_size
    output = [0] * len(arr)
    
    for i in arr:
        count_arr[i] += 1
    print(count_arr)
    
    for i in range(1, arr_size):
        count_arr[i] += count_arr[i - 1]
    print(count_arr)
    
countingSort([3, 4, 2, 2, 1, 10, 8, 8, 5, 3, 6])