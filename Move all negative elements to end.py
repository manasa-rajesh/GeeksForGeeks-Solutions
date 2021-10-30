class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        count = 0
        pos = []
        neg = []
        for ele in arr:
            if ele>=0:
                count += 1
                pos.append(ele)
            else:
                neg.append(ele)
        
        for i in range(count):
            arr[i] = pos[i]
            
        k = 0
        
        for i in range(count, n):
            arr[i] = neg[k]
            k += 1