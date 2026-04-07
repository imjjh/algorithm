import sys

n = int(sys.stdin.readline())

if n != 0:
    arr = []
    for i in range(n):
        arr.append(int(sys.stdin.readline()))

    k = int((0.15 * n)+0.5)

    arr.sort()

    print(int(sum(arr[k:len(arr)-k]) /  (len(arr)- 2*k)+0.5))

else:
    print(0)