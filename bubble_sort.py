def bubble_sort(lst):
    length = len(lst) - 1
    has_swapped = True
    iterations = 0
    
    while(has_swapped):
        has_swapped = False
        for i in range(length - iterations):
            if lst[i] > lst[i + 1]:
                lst[i + 1], lst[i] = lst[i], lst[i + 1]
        iterations += 1
    
    return lst
