class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        union = a + b
        union = set(union)
        return len(union)