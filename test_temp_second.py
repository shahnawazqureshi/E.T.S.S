import random
import time

li = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u"
, "v", "w", "x", "y"]

arr = {}

for k in range(0, 25):
    arr[li[k]] = [random.randrange(1, 10, 1) for i in range(1000000)]

start = time.perf_counter()

sum = 0
for k, v in arr.items():
    for value in v:
        sum += value 

end = time.perf_counter()

print(sum)

print("Finished in: ", round(end-start, 2), " seconds")