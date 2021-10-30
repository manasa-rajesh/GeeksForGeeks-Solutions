def rotate( arr, n):
    value = arr[-1]
    for i in reversed(range(1,n)):
        arr[i] = arr[i-1]
    arr[0] = value