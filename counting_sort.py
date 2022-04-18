def countingSort(arr):
    arr_size = max(arr) + 1
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
    
print(countingSort([3, 4, 2, 2, 1, 10, 8, 8, 5, 3, 6]))