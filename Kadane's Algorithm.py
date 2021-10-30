class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        maxi = 0
        current = 0
        count = 0
        for i in range(N):
            current += arr[i]
            if current > maxi:
                maxi = current
            if current < 0:
                current = 0
                count += 1
        if count == N:
            return max(arr)
        else:
            return maxi