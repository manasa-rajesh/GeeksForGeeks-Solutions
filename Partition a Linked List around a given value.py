class Solution:
    def partition(self, head, x):
        #code here
        ptr = head
        less = []
        equal = []
        more = []
        while(ptr != None):
            if ptr.data < x:
                less.append(ptr.data)
            elif ptr.data == x:
                equal.append(ptr.data)
            else:
                more.append(ptr.data)
            ptr = ptr.next
                
        nodes = less + equal + more
        
        ptr2 = head
        for i in range(len(nodes)):
            ptr2.data = nodes[i]
            ptr2 = ptr2.next
            
        return head