def bubble_sort(lst):
    length = len(lst) - 1
    has_swapped = True
    
    while(has_swapped):
        has_swapped = False
        for i in range(length):
            if lst[i] > lst[i + 1]:
                lst[i + 1], lst[i] = lst[i], lst[i + 1]
    return lst
