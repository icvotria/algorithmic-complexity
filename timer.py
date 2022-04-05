import time 

def bubble_sort(lst):
  length = len(lst) - 1
  for i in range(length):
        for j in range(length - i):
         if lst[i] > lst[j + 1]:
              lst[i + 1] = lst[i]
              lst[i] = lst[i + 1]
  print(lst)
            
  	

num_list = [34, 2, 76, 0, -1, 200]

def timer(algo, data):
	before = time.perf_counter()
	algo(data)
	after = time.perf_counter()
	total = after - before
	return total

print(timer(bubble_sort, num_list))
