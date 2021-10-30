def reverseArray(arr, n):
    l = arr.split(" ")
    m = []
    for i in reversed(range(n)):
        m.append(int(l[i]))
    return m
        
t = int(input())
for i in range(t):
    n = int(input())
    arr = input()
    for i in reverseArray(arr, n):
        print(i, end=" ")
    print('\n', end="")