import time 

def bubble_sort(lst):
  length = len(lst)
  for i in range(length):
  	print(lst[i])

num_list = [34, 2, 76, 0, -1, 200]

def timer():
	before = time.perf_counter()
	print(f"1: {before}")
	bubble_sort(num_list)
	after = time.perf_counter()
	total = after - before
	print(f"2:{after}")
	print(f"3: {total}")
 
# before = time.perf_counter()			
timer()
# after = time.perf_counter()
# print(after - before)
