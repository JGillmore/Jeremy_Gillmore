import random
import math
import time

def bubbleSort(arr, x):
    if x <= 0:
        print (time.time() - start)
        return arr
    for num in range(0,x):
        if arr[num] > arr[num+1]:
            arr[num], arr[num+1] = arr[num+1], arr[num]
    return bubbleSort(arr,x-1)

arr = []
for num in range(0,10000):
    arr.append(int(math.ceil(random.random()*10000)))

start = time.time()
# print bubbleSort(arr, len(arr)-1)
x = len(arr)
while (x >= 0):
    for num in range(0,x-1):
        if arr[num] > arr[num+1]:
            arr[num], arr[num+1] = arr[num+1], arr[num]
    x = x - 1
print arr
