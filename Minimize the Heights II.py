class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        maxi = 0
        mini = 0
        arr.sort()
        diff = arr[n-1] - arr[0]
        for i in range(1,n):
            if(arr[i] >= k):
                maxi = max(arr[i-1]+k, arr[n-1]-k)
                mini = min(arr[i]-k, arr[0]+k)
                diff = min(maxi-mini, diff)
        return diff