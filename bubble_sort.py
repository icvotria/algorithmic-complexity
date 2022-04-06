from timer import timer

num_list = [i for i in range(1000)]

def bubble_sort(lst):
    length = len(lst)
    for i in range(length):
        for j in range(length - 1):
            if lst[j] > lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
    print(lst)


print(timer(bubble_sort, num_list))
