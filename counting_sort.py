def countingSort(arr):
    arr_size = 15001
    count_arr = [0]*arr_size
    output = [0] * len(arr)
    
    for i in arr:
        count_arr[i] += 1
    
    for i in range(1, arr_size):
        count_arr[i] += count_arr[i - 1]
    
    i = len(arr) - 1
    
    while i >= 0:
        output[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1
        i -= 1
    
    return output
