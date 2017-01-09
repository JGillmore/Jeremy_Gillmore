def multiply(arr, num):
    count = 0
    while count < len(arr):
        arr[count] = arr[count] * num
        count += 1
    return arr

a = [2,4,10,16]

b = multiply(a, 5)
print b
