import time 

def bubble_sort(lst):
  length = len(lst)
  for i in range(length):
  	print(lst[i] * 128751235246)

num_list = [34, 2, 76, 0, -1, 200]

def timer(algo, data):
	before = time.perf_counter()
	print(before)
	algo(data)
	after = time.perf_counter()
	print(after)
	total = after - before
	return total
 
print(timer(bubble_sort, num_list))
