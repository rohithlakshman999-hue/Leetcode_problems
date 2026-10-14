# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        a = []
        temp=head
        while temp is not None:
            a.append(temp.val)
            temp=temp.next 
    
        temp=head
        while temp is not None:
            if temp.val != a[-1]:
                return False
            a.pop()
            temp=temp.next
        return True
        
        