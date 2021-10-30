def getNthFromLast(head,n):
    #code here
    ptr = head
    nodes = []
    while(ptr != None):
        nodes.append(ptr.data)
        ptr = ptr.next
    k = len(nodes)
    if k-n < 0:
        return -1
    else:
        return nodes[k-n]