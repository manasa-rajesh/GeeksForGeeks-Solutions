class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, s):
        # Code here
        temp = []
        while(len(s)!=0):
            k = s.pop()
            while(len(temp)!=0 and temp[len(temp)-1]<k):
                s.append(temp.pop())
            temp.append(k)
        for i in range(len(temp)):
            s.append(temp.pop())