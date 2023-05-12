x = int(input("Enter Start range:"))
y = int(input("Enter End range:"))
print("Range", x, "to", y,)
for N in range(x, y + 1):
    n = 0
    for i in range(2, N):
        if N % i == 0:
            n = 1
            break
    if n == 0:
        print(N, end=" ")
