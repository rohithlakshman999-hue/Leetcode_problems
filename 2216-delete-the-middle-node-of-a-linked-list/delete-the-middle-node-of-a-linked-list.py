# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if(head.next==None):
            return None  
        temp=head
        i=0
        while temp is not None:
            temp=temp.next
            i+=1
        
        n=i/2
        b=0
        temp=head
        while b<n-1:
            b+=1
            temp=temp.next
        temp.next=temp.next.next
        return head
