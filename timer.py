import time

def timer(algo, data):
	before = time.perf_counter()
	algo(data)
	after = time.perf_counter()
	total = after - before
	return total