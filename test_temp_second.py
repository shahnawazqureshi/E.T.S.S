import random 

temp_ran = [[i, j]  for i in range(1, 6) for j in range(1, 5)]
random.shuffle(temp_ran)
print(temp_ran)
print(len(temp_ran))


# import threading
# import time

# li = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u"
# , "v", "w", "x", "y"]

# arr = {}
# results = {}
# for k in range(0, 25):
#     arr[li[k]] = [random.randrange(1, 10, 1) for i in range(1000000)]
#     results[li[k]] = 0

# def FindRowSum(dic, row, results):
#     sum = 0
#     for item in dic[row]:
#         sum = sum + item   
#     results[row] = sum

# start = time.perf_counter()

# allThreads = []
# for row in range(0, len(li)):
#     thread = threading.Thread(target=FindRowSum, args=(arr, li[row], results))
#     allThreads.append(thread)
#     thread.start()

# # for k, v in arr.items():
# #     for value in v:
# #         sum += value 

# for thread in allThreads:
#     thread.join()
# # sum = 0
# # for _, k in arr.items():
# #     sum = sum + k
# # print(sum)
# end = time.perf_counter()

# # print(sum)

# print("Finished in: ", round(end-start, 2), " seconds")