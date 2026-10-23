# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        temp=list1
        ans=[]
        while temp is not None:
            ans.append(temp.val)
            temp=temp.next
        
        temp=list2
        while temp is not None:
            ans.append(temp.val)
            temp=temp.next
        
        ans.sort()
        dummy=ListNode(0)
        temp=dummy
        for i in range(len(ans)):
            temp.next=ListNode(ans[i])
            temp=temp.next
        return dummy.next