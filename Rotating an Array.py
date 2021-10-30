class Solution:
    def leftRotate(self, arr, n, d):
        temp = arr[0:d]
        del arr[:d]
        arr.extend(temp)
        return arr