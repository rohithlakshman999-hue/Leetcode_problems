# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        temp=head
        a=[]
        while temp is not None:
            a.append(temp.val)
            temp=temp.next
        
        a.sort()
        i=0
        temp=head
        while temp is not None:
            temp.val=a[i]
            i+=1
            temp=temp.next
        return head
        