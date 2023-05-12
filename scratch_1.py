import math
import array

"""
arr = array.array('i', [])
for i in range(1, 50):
    for j in range(1, 50):
        if math.sqrt(j) == i:
            arr.append(i * i)
            break
for k in range(len(arr)):
    print(arr[k])
"""


x = int(input("Enter a starting range: "))
y = int(input("  Enter a ending range: "))
for i in range(x, y):
    for j in range(x, y):
        if math.sqrt(j) == i:
            prinzzzzzzzzz