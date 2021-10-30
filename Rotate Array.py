def rotate(arr, n, d):
    temp = arr[0:d]
    arr = arr[d:]
    arr.extend(temp)
    result = ' '.join([str(elem) for elem in arr])
    return result
    
t = int(input())
for i in range(t):
    val = input()
    val = list(val.split(" "))
    val = list(filter(None, val))
    val = list(map(int, val))
    N = val[0]
    D = val[1]
    arr = input()
    arr = list(arr.split(" "))
    arr = list(filter(None, arr))
    arr = list(map(int, arr))
    print(rotate(arr, N, D))