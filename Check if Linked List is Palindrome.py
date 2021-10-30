class Solution:
    def isPalindrome(self, head):
        l = []
        while(head != None):
            l.append(head.data)
            head = head.next
        reverse = [ele for ele in reversed(l)]
        if l == reverse:
            return True
        else:
            return False