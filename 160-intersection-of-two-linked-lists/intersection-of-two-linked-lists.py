# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        temp=headA
        s=set()
        while temp is not None:
            s.add(temp)
            temp=temp.next
        
        temp=headB
        while temp is not None:
            if temp in s:
                return temp
            temp=temp.next
        return None
        