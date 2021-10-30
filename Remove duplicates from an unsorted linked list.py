class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        current = head
        prev = None
        duplicates = {}
        while current:
            if current.data in duplicates:
                prev.next = current.next
                current = None
            else:
                duplicates[current.data] = 1
                prev = current
            current = prev.next
        return head