def deleteMid(head):
    '''
    head:  head of given linkedList
    return: head of resultant llist
    '''
    ptr1 = None
    ptr2 = None
    
    ptr1 = head
    ptr2 = head
    
    prev = None
    
    
    
    while(ptr1 != None and ptr1.next != None):
        ptr1 = ptr1.next.next
        prev = ptr2
        ptr2 = ptr2.next
    
    prev.next = ptr2.next
    
    return head