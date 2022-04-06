def bubble_sort(lst):
    
    length = len(lst)
    for i in range(length):
        for j in range(length - 1):
            if lst[j] > lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
    return lst
